import os
import sys
import argparse

import termcolor

from fileclass import File


parser = argparse.ArgumentParser(
    description="Terminal command using XOR algorithm to encrypt/decrypt files"
)

parser.add_argument(
    "-f",
    "--file",
    type=str,
    help="the file you want to encrypt/decrypt"
)

parser.add_argument(
    "-p",
    "--password",
    type=str,
    help="the password you want to encrypt/decrypt the file with"
)

parser.add_argument(
    "--replace",
    action="store_true",
    help="to use if you want to replace the original file"
)

args = parser.parse_args()


if not args.file:
    warning_text = termcolor.colored(f"[/!\\] No file was given, process interrupted...\n", "yellow")
    print(warning_text)
    parser.print_help()
    sys.exit(1)

if not os.path.exists(args.file) or not os.path.isfile(args.file):
    error_text = termcolor.colored(f"[!] File '{args.file}' was not found...\n", "red")
    print(error_text)
    sys.exit(2)

if not args.password:
    warning_text = termcolor.colored(f"[/!\\] No password was given, process interrupted...\n", "yellow")
    print(warning_text)
    parser.print_help()
    sys.exit(3)


file = File(args.file)

file.xor_crypt(
    password=args.password,
    replace_file=args.replace
)
