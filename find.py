# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="case-insensitive")

    args = parser.parse_args()

    if args.ignore_case:
        args.pattern = args.pattern.lower()

    with open(args.filename) as file:
        content = file.read()

        lines = content.split("\n")

        for i in range(len(lines)):
            line = lines[i]

            if (args.ignore_case):
                line = line.lower()

            if args.pattern in line:
                print(f"{i+1}: {lines[i]}")


if __name__ == "__main__":
    main()
