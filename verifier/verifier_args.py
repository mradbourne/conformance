import argparse
from conformance_cli.argparsers.testdriver_verifier_common import (
    add_testdriver_verifier_common_args,
)


class VerifyArgs:
    def __init__(self, args):
        self.parser = argparse.ArgumentParser(
            description="Process DDT Verifier arguments"
        )

        add_testdriver_verifier_common_args(self.parser)

        # Specific for verifier
        self.parser.add_argument(
            "--verify_all",
            action="store_true",
            help="Verify all available report files",
            default=None,
        )

        self.parser.add_argument(
            "--summary_only",
            action="store_true",
            help="Flag to create summaries from current reports",
            default=None,
        )

        self.parser.add_argument(
            "--test_verifier", help="Flag to run in test mode", default=None
        )

        self.parser.add_argument(
            "--run_serial",
            default=None,
            help="Set if execution should be done serially. Parallel is the default.",
        )

        self.options = self.parser.parse_args(args)
        return

    def getOptions(self):
        return self.options
