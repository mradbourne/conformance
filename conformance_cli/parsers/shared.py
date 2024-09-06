from ..config import test_types


def add_generic_arguments(parser):
    parser.add_argument("--icu_versions", nargs="*", default=[])
    parser.add_argument(
        "--test_types",
        nargs="*",
        choices=test_types,
        default=test_types,
    )
    parser.add_argument("--run_serial", action="store_true")
