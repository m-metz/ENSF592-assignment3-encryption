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
    """Runs the ENSF 592 encryption command line interface program.

    It can encode and decode text given a cipher that maps to 26 lowercase english letters.
    """
    
    print("")
    print("ENSF 592 Encryption Program")
    print("Use Ctrl+C to quit.")
    print("")

    try:
        cli = CommandLineInterface()
        mapping_cipher = cli.prompt_for_cipher_text()
        decoded_or_encoded_text = cli.prompt_for_text_to_encode_decode()
        encoded_or_decoded_text = mapping_cipher.encode_decode_text(decoded_or_encoded_text)
        cli.display_encoded_or_decoded_text(encoded_or_decoded_text)

    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()

