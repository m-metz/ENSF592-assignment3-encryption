"""Command Line Interface Module
Author: Michael Metz
"""

from enum import auto, Enum
import re
from text_codec.decoded_text import DecodedText
from text_codec.encoded_text import EncodedText
from text_codec.mapping_cipher import CIPHER_LENGTH, MappingCipher

class encodeDecodeMode(str, Enum):
    NOT_SET = auto()
    ENCODE = "encode"
    DECODE = "decode"

class CommandLineInterface:
    """
    """

    """Encode Decode mode"""
    __encode_decode_mode = encodeDecodeMode.NOT_SET
    __mapping_cipher = None
    encoded_text = None
    decoded_text = None

    """ Prompt for encode decode mode"""
    def prompt_for_encode_decode_mode(self):
        re_encode_decode_mode = re.compile("^[eEdD]$")
        input_text = ""
       
        while True:
            input_text = input("Enter 'e' to encode your text or 'd' to decode"
                + " your text (case-insensitive): ")
            # match() looks at start of string and search() searches all of the
            # string, but we only want one character, so match() is fine
            if re_encode_decode_mode.match(input_text) is not None:
                break

            print("You must enter 'e' or 'd'")
        
        re_encode_mode = re.compile("^[eE]$")

        # Since we know input_text is regex_encode_decode_mode, we only have to
        # check if it's encode mode, else it is decode mode.
        if re_encode_mode.match(input_text) is not None:
            self.__encode_decode_mode = encodeDecodeMode.ENCODE
        else:
            self.__encode_decode_mode = encodeDecodeMode.DECODE

    """Prompt for cipher"""
    def prompt_for_cipher(self):
        CIPHER_CRITERIA_STRING = "must be exactly " + str(CIPHER_LENGTH) + " unique lowercase letters or numbers"
        input_text = ""
        encode_decode_string = ""

        if self.__encode_decode_mode == encodeDecodeMode.ENCODE:
            encode_decode_string = encodeDecodeMode.ENCODE.value
        elif self.__encode_decode_mode == encodeDecodeMode.DECODE:
            encode_decode_string = encodeDecodeMode.DECODE.value

        input_text = input("Enter the cipher text to be "
                + encode_decode_string + "d (" + CIPHER_CRITERIA_STRING + "): ")

        while True:
            try:
                self.__mapping_cipher = MappingCipher(input_text)
            except ValueError as exception:
                print(exception)
            else: # Cipher is valid, no ValueError
                break
            input_text = input("Please re-enter a valid cipher (" + CIPHER_CRITERIA_STRING + "): ")
            

    """Prompt for text to encode/decode"""
    def prompt_for_text_to_encode_decode(self):
        input_text = ""
        
        if self.__encode_decode_mode == encodeDecodeMode.ENCODE:
            input_text = input("Enter the text to be encoded (case-insensitive): ")
            
            self.decoded_text = DecodedText(input_text)

        elif self.__encode_decode_mode == encodeDecodeMode.DECODE:
            input_text = input("Enter the text to be decoded (case-insensitive): ")

            while True:
                try:
                    self.encoded_text = EncodedText(input_text)
                except ValueError as exception:
                    print(exception)
                else: # EncodedText is valid, no ValueError
                    break
                input_text = input("Please re-enter valid encoded text: ")

    def encode_decode_text(self):
        if self.__encode_decode_mode == encodeDecodeMode.ENCODE:
            self.__mapping_cipher.encode(self.decoded_text)
        elif self.__encode_decode_mode == encodeDecodeMode.DECODE:
            self.__mapping_cipher.decode(self.encoded_text)