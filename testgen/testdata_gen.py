# -*- coding: utf-8 -*-
import multiprocessing as mp
import re
import logging

from conformance_cli.config import TestType
from .generators.collation_short import CollationShortGenerator
from .generators.datetime_fmt import DateTimeFmtGenerator
from .generators.lang_names import LangNamesGenerator
from .generators.likely_subtags import LikelySubtagsGenerator
from .generators.message_fmt2 import MessageFmt2Generator
from .generators.list_fmt import ListFmtGenerator
from .generators.number_fmt import NumberFmtGenerator
from .generators.plurals import PluralGenerator
from .generators.relativedatetime_fmt import RelativeDateTimeFmtGenerator

logger = logging.getLogger(__name__)
reblankline = re.compile("^\s*$")


def generate_versioned_data_parallel(args):
    num_processors = mp.cpu_count()
    logger.info(
        "Test data generation: %s processors for %s plans",
        num_processors,
        len(args.icu_versions),
    )

    version_data = []
    for icu_version in args.icu_versions:
        version_data.append({"icu_version": icu_version, "args": args})

    processor_pool = mp.Pool(num_processors)
    with processor_pool as p:
        result = p.map(generate_versioned_data, version_data)

    return result


def generate_versioned_data(version_info):
    args = version_info["args"]
    icu_version = version_info["icu_version"]

    logger.info(
        "Generating .json files for data driven testing. ICU_VERSION requested = %s",
        icu_version,
    )

    if len(args.test_types) < len(TestType):
        logger.info("(Only generating %s)", ", ".join(args.test_types))

    if TestType.COLLATION_SHORT in args.test_types:
        # This is slow
        generator = CollationShortGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    # DISABLED FOR NOW. Use new .js generator with Node version
    if TestType.DATETIME_FMT in args.test_types:
        # This is slow
        generator = DateTimeFmtGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.LIST_FMT in args.test_types:
        # This is slow
        generator = ListFmtGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.LANG_NAMES in args.test_types:
        # This is slow
        generator = LangNamesGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.LIKELY_SUBTAGS in args.test_types:
        generator = LikelySubtagsGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.MESSAGE_FMT2 in args.test_types:
        generator = MessageFmt2Generator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.NUMBER_FMT in args.test_types:
        generator = NumberFmtGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.RELATIVE_DATETIME_FMT in args.test_types:
        # This is slow
        generator = RelativeDateTimeFmtGenerator(icu_version, args.gen_limit)
        generator.process_test_data()

    if TestType.PLURAL_RULES in args.test_types:
        # This is slow
        generator = PluralGenerator(icu_version, args.gen_limit)
        generator.process_test_data()
    logger.info("++++ Data generation for %s is complete.", icu_version)


def run(args):
    logger.info("Generating test data...")
    if args.run_serial:
        logger.warn(
            "'run_serial' is set"
            + " but test data generation always runs in parallel if possible."
        )

    generate_versioned_data_parallel(args)
