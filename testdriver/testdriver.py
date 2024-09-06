# Read a Data Driven Test file
# 1. Parse into JSON structure
# 2. For each test, stringify and output as single line to stdout

from datetime import datetime
import json

import multiprocessing as mp

import os
import subprocess
import sys
import logging

import datasets as ddt_data
import ddtargs

from testplan import TestPlan

logger = logging.getLogger(__name__)

# TODO: Separate TestPlan into another module.


class TestDriver:
    def __init__(self):
        # All test plans requested from command line arguments
        self.cldrVersion = None
        self.icuVersion = None
        self.test_plans = []
        self.debug = False

        self.run_serial = False  # Default is to operate in parallel

        return

    def set_args(self, arg_options):
        # Options come from parse of command line
        self.icuVersion = arg_options.icu_version
        self.cldrVersion = arg_options.cldr

        self.run_serial = arg_options.run_serial

        # Create "test plans" for each option
        for test_type in arg_options.test_type:

            if test_type not in ddt_data.testDatasets:
                logger.warning(
                    "**** WARNING: test_type %s not in testDatasets", test_type
                )
            else:
                # Create a test plan based on data and options
                test_data_info = ddt_data.testDatasets[test_type]
                if self.debug:
                    logger.info(
                        "$$$$$ test_type = %s test_data_info = %s",
                        test_type,
                        test_data_info.testDataFilename,
                    )

                for executor in arg_options.exec:
                    if not ddt_data.allExecutors.has(executor):
                        # Run a non-specified executor. Compatibility of versions
                        # between test data and the executor should be done the text executor
                        # program itself.
                        logger.error(
                            "No executable command configured for executor platform: %s",
                            executor,
                        )
                        exec_command = {"path": executor}
                    else:
                        # Set details for execution from ExecutorInfo
                        resolved_cldr_version = ddt_data.resolveCldr(self.cldrVersion)
                        exec_command = ddt_data.allExecutors.versionForCldr(
                            executor, resolved_cldr_version
                        )
                        # The command needs to be something else!

                    new_plan = TestPlan(exec_command, test_type)
                    new_plan.set_options(arg_options)
                    new_plan.test_lang = executor.split()[0]

                    try:
                        test_data = ddt_data.testDatasets[test_type]
                        new_plan.set_test_data(test_data)
                    except KeyError as err:
                        logger.warning(
                            "!!! %s: No test data filename for %s", err, test_type
                        )

                    if not new_plan.ignore:
                        self.test_plans.append(new_plan)

    def parse_args(self, args):
        # TODO: handle arguments for:
        #   executor language: NODE, RUST, CPP, JAVA, ETC.
        #   CLDR version
        #   test types: e.g., "collator", "decimal", "datetime", etc.
        #   Use these to get dataset info and call appropriate routines
        #     to execute tests and verify results.

        # Get all the arguments
        argparse = ddtargs.DdtArgs(args)
        if self.debug:
            logger.info("TestDriver OPTIONS: %s", argparse.getOptions())

        # Now use the argparse.options to set the values in the driver
        self.set_args(argparse.getOptions())
        return

    def run_plans(self):
        # For each of the plans, run with the appropriate type of parallelism
        # Debugging output
        for plan in self.test_plans:
            plan.run_plan()

    def run_one(self, plan):
        logger.info(
            "Parallel of %s %s %s" % (plan.test_lang, plan.test_type, plan.icu_version)
        )
        plan.run_plan()

    def run_plans_parallel(self):
        # Testing 15-Jan-2024
        num_processors = mp.cpu_count()
        logger.info(
            "There are %s processors for %s plans"
            % (num_processors, len(self.test_plans))
        )

        processor_pool = mp.Pool(num_processors)
        with processor_pool as p:
            p.map(self.run_one, self.test_plans)


def run(args):
    logger.info("Executing tests...")
    driver = TestDriver()

    if args.run_serial:
        driver.run_plans()
    else:
        driver.run_plans_parallel()
