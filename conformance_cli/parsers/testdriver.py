from .shared import add_generic_arguments
from ..config import executors


def add_testdriver_subparser(subparsers):
    parser = subparsers.add_parser("run")
    add_generic_arguments(parser)
    parser.add_argument(
        "--run_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )
    parser.add_argument(
        "--exec",
        nargs="*",
        choices=executors,
        default=executors,
    )
