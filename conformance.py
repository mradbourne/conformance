import os
import sys
import argparse

DOCKER_CMD = (
    "docker run --rm -v .:/conformance -it $(docker build -t conformance:latest -q .)"
)


def main():
    parser = argparse.ArgumentParser(
        prog="Unicode Conformance",
        description="Unicode & CLDR Data Driven Test",
        epilog="This is an experimental CLI.",
    )

    parser.add_argument(
        "--containerize", action=argparse.BooleanOptionalAction, default=True
    )
    parser.add_argument(
        "action", help="Action to perform", choices=["shell", "generate"]
    )
    args = parser.parse_args()

    if args.action == "shell":
        print(DOCKER_CMD)
        os.system(DOCKER_CMD)
        return

    if args.containerize:
        rerun_in_container()
        return

    print(args)


def rerun_in_container():
    cmd = " ".join(
        [
            DOCKER_CMD,
            f"python3 {os.path.basename(__file__)} --no-containerize",
            *sys.argv[1:],
        ]
    )
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    main()
