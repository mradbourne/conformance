import os
import sys
import argparse


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
        cmd = "docker run --rm -it $(docker build -t conformance:latest -q .)"
        print(cmd)
        os.system(cmd)
        return

    if args.containerize:
        rerun_in_container()
        return

    print(args)


def rerun_in_container():
    cmd = " ".join(
        [
            "docker run --rm -it $(docker build -t conformance:latest -q .)",
            "python3 conformance.py --no-containerize",
            *sys.argv[1:],
        ]
    )
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    main()
