"""Command Line Interface Module
Author: Michael Metz
"""


import re
from text_codec.decoded_text import DecodedText
from text_codec.encoded_text import EncodedText
from text_codec.mapping_cipher import CIPHER_LENGTH, EncodeDecodeMode, MappingCipher


class CommandLineInterface:
    """This is the command line interface the user interacts with. It is
    responsible for receiving, validating or delegating the validating of
    user input, and displaying output to the user.

    Prompts for the encode decode mode and assigns it to the
    __mapping_cipher.
    
    This prompting is in the constructor because this class depends on the
    __mapping_cipher.encode_decode_mode.
    """
    
    __mapping_cipher = MappingCipher()

    def __init__(self):
        re_encode_decode_mode = re.compile("^[eEdD]$")
        input_text = ""

        while True:
            input_text = input("Enter 'e' to encode your text or 'd' to decode"
                + " your text (case-insensitive): ")
            
            """
            match() looks at start of string and search() searches all of the
            string, but we only want one character, so match() is fine
            """
            if re_encode_decode_mode.match(input_text) is not None:
                break

            print("You must enter 'e' or 'd'")

        re_encode_mode = re.compile("^[eE]$")

        """
        Since we know input_text is regex_encode_decode_mode, we only have to
        check if it's encode mode, else it is decode mode.
        """
        if re_encode_mode.match(input_text) is not None:
            self.__mapping_cipher.encode_decode_mode = EncodeDecodeMode.ENCODE
        else:
            self.__mapping_cipher.encode_decode_mode = EncodeDecodeMode.DECODE
    
    def __mapping_cipher_not_set():
        """
        Raises:
            ValueError: When __mapping_cipher.encode_decode_mode is not set.
        """

        raise ValueError("__mapping_cipher.encode_decode_mode is not set.")

    def prompt_for_cipher_text(self):
        """Prompt for cipher text
        
        Returns:
            The CLI's __mapping_cipher with a valid cipher_text set.

        Raises:
            ValueError: If __mapping_cipher.encode_decode_mode is not set
            (which should never happen as the CommandLineInterface() constuctor
            sets it).
        """

        CIPHER_CRITERIA_STRING = "must be exactly " + \
            str(CIPHER_LENGTH) + " unique lowercase letters or numbers"
        input_text = ""
        encode_decode_string = ""

        if self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.ENCODE:
            encode_decode_string = EncodeDecodeMode.ENCODE.value + "d"
        elif self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.DECODE:
            encode_decode_string = EncodeDecodeMode.DECODE.value + "d"
        else:
            self.__mapping_cipher_not_set()

        input_text = input("Enter the cipher text to be "
            + encode_decode_string + " (" + CIPHER_CRITERIA_STRING + "): ")

        while True:
            try:
                self.__mapping_cipher.cipher_text = input_text
            except ValueError as exception:
                print(exception)
            else:  # Cipher is valid, no ValueError
                break
            input_text = input(
                "Please re-enter a valid cipher (" + CIPHER_CRITERIA_STRING + "): ")

        return self.__mapping_cipher

    def prompt_for_text_to_encode_decode(self):
        """Prompt for text to encode/decode unless the
        __mapping_cipher.encode_decode_mode is not set

        Returns:
            Either an EncodedText (to decode) or a DecodedText (to encode)
            depending on __mapping_cipher.encode_decode_mode
        
        Raises:
            ValueError: If __mapping_cipher.encode_decode_mode is not set
            (which should never happen as this classes constuctor sets it).
        """

        input_text = ""

        if self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.ENCODE:
            input_text = input(
                "Enter the text to be encoded (case-insensitive): ")

            # DecodedText is always valid, and non-alphanumeric characters will
            # be removed.
            return DecodedText(input_text)
        elif self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.DECODE:
            input_text = input(
                "Enter the text to be decoded (lowercase alphanumeric and "
                    + " it should only contain characters that are in the "
                    + "cipher): ")
            encoded_text = ""

            while True:
                try:
                    encoded_text = EncodedText(input_text)
                except ValueError as exception:
                    print(exception)
                else:  # EncodedText is valid, no ValueError
                    break
                input_text = input("Please re-enter valid encoded text: ")

            return encoded_text
        else:
            self.__mapping_cipher_not_set()

    def display_encoded_or_decoded_text(self, encoded_or_decoded_text):
        """Displays the encoded or decoded text to the user.

        Args:
            encoded_or_decoded_text (EncodedText or DecodedText): The text to
                encode or decode.

        Raises:
            ValueError: If __mapping_cipher.encode_decode_mode is not set
            (which should never happen as the CommandLineInterface() constuctor
            sets it).
        """
        if self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.ENCODE:
            print("Your encoded text is: " + encoded_or_decoded_text)
        elif self.__mapping_cipher.encode_decode_mode == EncodeDecodeMode.DECODE:
            print("Your decoded text is: " + encoded_or_decoded_text)
        else:
            self.__mapping_cipher_not_set()