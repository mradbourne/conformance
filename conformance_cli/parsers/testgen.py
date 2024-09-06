from .shared import add_generic_arguments


def add_testgen_subparser(subparsers):
    parser = subparsers.add_parser("testgen")
    add_generic_arguments(parser)
    parser.add_argument(
        "--gen_limit", nargs="?", type=int, default=-1  # -1 is no limit
    )
