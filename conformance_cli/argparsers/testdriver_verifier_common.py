from .. import config


# Set up arguments common to both testDriver and verifier
def add_testdriver_verifier_common_args(parser):

    # All more than one item in exec list
    parser.add_argument(
        "--exec",
        nargs="*",
        choices=config.executors,
        default=config.executors,
        help="Execution platforms",
    )

    parser.add_argument("--environment", help="Environment variables, e.g., 'a=x;b=y'")

    # TODO: are these being used? How?
    parser.add_argument("--icu", default="LATEST")
    parser.add_argument("--cldr", default="LATEST")

    # Location of the data files
    parser.add_argument(
        "--file_base",
        default="",
        help="Base directory for input, output, and report paths",
    )
    parser.add_argument("--input_path", default=config.paths["default_input"])
    parser.add_argument("--output_path", default=config.paths["default_output"])
    parser.add_argument("--report_path", default=config.paths["default_report"])

    parser.add_argument("--exec_mode", default="one_test")
    parser.add_argument("--parallel_mode", default=None)
    parser.add_argument("--run_limit", default=None)

    # Arguments for setting versions of executors
    parser.add_argument(
        "--node_version", default="node"
    )  # Sets the version of node to test
    parser.add_argument("--icu4x_version", default="latest")
    parser.add_argument("--icu4c_version", default="latest")
    parser.add_argument("--icu4j_version", default="latest")

    parser.add_argument(
        "--custom_testfile",
        default=None,
        action="extend",
        nargs="*",
        help="full path to test data file in JSON format",
    )

    parser.add_argument(
        "--progress_interval",
        help="Interval between progress output printouts",
        default=None,
    )

    parser.add_argument("--debug_level", default=None)

    parser.add_argument("--ignore", default=None)
