import os
import sys
import argparse

from .test_type import test_types


DOCKER_CMD = (
    "docker run --rm -v .:/conformance -it $(docker build -t conformance:latest -q .)"
)


def run():
    args = parse_args()

    if args.containerize:
        rerun_in_container()
        return

    print(args)


def parse_args():
    parser = argparse.ArgumentParser()

    # Which actions to perform
    parser.add_argument(
        "--testgen", action=argparse.BooleanOptionalAction, default=True
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


def rerun_in_container():
    cmd = " ".join(
        [
            DOCKER_CMD,
            "python3 conformance.py --no-containerize",
            *sys.argv[1:],
        ]
    )
    print(cmd)
    os.system(cmd)
