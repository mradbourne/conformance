import os
import sys
import argparse

from .config import test_types, executors

DOCKER_BUILD_CMD = "docker build -t conformance:latest ."
DOCKER_RUN_CMD = "docker run --rm -v .:/conformance -it conformance:latest"


def run():
    args = parse_args()

    if args.shell:
        run_in_docker("bash")
        return

    if args.containerize:
        rerun_in_container()
        return

    # Importing after containerizing to avoid missing dependencies
    from testgen import testdata_gen

    if args.testgen:
        testdata_gen.run(args)

    if args.exec:
        print("TODO: Invoke testdriver with args", args.exec)


def parse_args():
    parser = argparse.ArgumentParser()

    # Which actions to perform
    parser.add_argument(
        "--testgen", action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument(
        "--exec",
        nargs="*",
        choices=executors,
        default=executors,
    )
    parser.add_argument("--no-exec", dest="exec", action="store_false")

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
        "--testgen_run_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )
    parser.add_argument(
        "--exec_run_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )
    parser.add_argument("--run_serial", action="store_true")
    parser.add_argument(
        "--containerize", action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument("--shell", action="store_true")

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
