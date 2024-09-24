from .common import add_common_args


def add_testgen_subparser(subparsers):
    parser = subparsers.add_parser("testgen")
    add_common_args(parser)
    parser.add_argument(
        "--gen_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )
