from ..config import test_types
from testdriver.datasets import icu_version_names


def add_common_args(parser):
    parser.add_argument("--icu_version", choices=icu_version_names)
    parser.add_argument(
        "--test_types",
        "--test_type",
        "--type",
        "--test",
        "-t",
        nargs="*",
        choices=test_types,
        default=test_types,
    )
    parser.add_argument(
        "--run_serial",
        action="store_true",
        help="Set if execution should be done serially. Parallel is the default.",
    )
