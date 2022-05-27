# encryption.py
# Michael Metz
#
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import sys
from text_codec.command_line_interface import CommandLineInterface

def main():
    print("")
    print("ENSF 592 Encryption Program")
    print("Use Ctrl+C to quit.")
    print("")

    cli = CommandLineInterface()
    try:
        cli.prompt_for_encode_decode_mode()
        cli.prompt_for_cipher()
        cli.prompt_for_text_to_encode_decode()
        cli.encode_decode_text()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()

