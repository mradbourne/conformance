import os
import sys
import argparse

from .argparsers.testdriver import add_testdriver_subparser
from .argparsers.testgen import add_testgen_subparser
from .config import init_config

DOCKER_BUILD_CMD = "docker build -t conformance:latest ."
DOCKER_RUN_CMD = "docker run --rm -v .:/conformance -it conformance:latest"


def run():
    init_config()
    args = parse_args()

    if args.command == "shell":
        run_in_docker("bash")
        return

    if args.containerize:
        rerun_in_container()
        return

    # Importing after containerizing to avoid missing dependencies
    from testgen import testdata_gen
    from testdriver import testdriver

    if args.command == "testgen":
        testdata_gen.run(args)

    if args.command == "run":
        testdriver.run(args)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--containerize", action=argparse.BooleanOptionalAction, default=True
    )

    subparsers = parser.add_subparsers(dest="command")
    add_testgen_subparser(subparsers)
    add_testdriver_subparser(subparsers)
    subparsers.add_parser("shell")

    return parser.parse_args()


def rerun_in_container():
    run_in_docker(
        "python3 conformance.py --no-containerize",
        *sys.argv[1:],
    )


def run_in_docker(*docker_args):
    print(DOCKER_BUILD_CMD)
    os.system(DOCKER_BUILD_CMD)

    cmd = " ".join([DOCKER_RUN_CMD, *docker_args])
    print(cmd)
    os.system(cmd)
