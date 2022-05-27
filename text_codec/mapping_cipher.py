"""Mapping Cipher Module
Author: Michael Metz
"""

import re

class MappingCipher:
    
    CIPHER_LENGTH = 26
    
    cipher_text = ""

    def __init__(self, input_text):
        re_exactly_n_alphanumeric = re.compile("^[a-z0-9]{" + str(CIPHER_LENGTH)
            + "}$")
        if re_exactly_n_alphanumeric.match(input_text) is None:
            raise ValueError("Cipher does not contain " + str(CIPHER_LENGTH)
                + " characters or contains characters that are not lowercase "
                + "letters or numbers.")
        elif not self.__unique_characters(input_text):
            raise ValueError("Cipher containes non-unique characters")

        self.cipher_text = input_text

    # This code is derived from https://stackoverflow.com/a/17357428/1873164
    # Sets only store unique characters, so if a set equals a string of chars,
    # it has unique characters
    def __unique_characters(self, text):
       return len(set(text)) == len(text)

    def encode(self, input_text):
        pass

    def decode(self, input_text):
        pass


CIPHER_LENGTH = MappingCipher.CIPHER_LENGTH