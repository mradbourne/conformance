import argparse
from conformance_cli.test_type import test_types


def parse_args():
    parser = argparse.ArgumentParser()

    # Which actions to perform
    parser.add_argument(
        "--generate", action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument(
        "--execute", action=argparse.BooleanOptionalAction, default=True
    )

    # Which tests to perform the action(s) on
    parser.add_argument("--icu_versions", nargs="*", default=[])
    parser.add_argument(
        "--test_types",
        nargs="*",
        choices=test_types,
        default=test_types,
    )

    # Other configuration options
    parser.add_argument(
        "--containerize", action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument(
        "--testgen_run_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )

    return parser.parse_args()


def run():
    args = parse_args()
    print(args)
