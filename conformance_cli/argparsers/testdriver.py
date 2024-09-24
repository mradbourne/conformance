from .common import add_common_args
from .testdriver_verifier_common import add_testdriver_verifier_common_args


def add_testdriver_subparser(subparsers):
    parser = subparsers.add_parser("run")
    add_common_args(parser)
    add_testdriver_verifier_common_args(parser)
