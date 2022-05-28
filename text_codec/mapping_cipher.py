"""Mapping Cipher Module
Author: Michael Metz
"""

from enum import auto, Enum
import re

class EncodeDecodeMode(Enum):
    """An Enum to track the if a class is in ENCODE or DECODE mode. NOT_SET can
    be used as a default value until the mode is set.

    Attributes:
        NOT_SET: The mode has not been set.
        ENCODE: The mode is encode mode.
        DECODE: The mode is decode mode.
    """
    NOT_SET = auto()
    ENCODE = "encode"
    DECODE = "decode"

class MappingCipher:
    """A Mapping Cipher class that is capable of tracking whether to encode or
    decode. It takes a cipher text, validates it, and uses it to encode and
    decode decoded text and encoded text.

    Attributes:
        encode_decode_mode (EncodeDecodeMode): The mode the class will run in.
        cipher_text (str): The cipher text to encode or decode with.
        CIPHER_LENGTH (int): The length of the mapping cipher.
    """
    CIPHER_LENGTH = 26
    """CIPHER_LENGTH (int): The length of the mapping cipher."""
    
    __encode_decode_mode = EncodeDecodeMode.NOT_SET
    __cipher_text = ""

    @property
    def encode_decode_mode(self):
        """encode_decode_mode (EncodeDecodeMode): Get or set the encode decode
        mode
        """
        return self.__encode_decode_mode

    @encode_decode_mode.setter
    def encode_decode_mode(self, encode_decode_mode):
        self.__encode_decode_mode = encode_decode_mode

    @property
    def cipher_text(self):
        """cipher_text (str): Set the cipher text

        Raises:
            AttributeError: When cipher_text is read from.
            ValueError: When the cipher_text is not CIPHER_LENGTH alphanumeric
                characters. Also occurs if the cipher characters are not
                unique.
        """
        raise AttributeError("cipher_text can only be written to, not read.")

    @cipher_text.setter
    def cipher_text(self, input_text):
        re_exactly_n_alphanumeric = re.compile("^[a-z0-9]{" + str(CIPHER_LENGTH)
            + "}$")
        if re_exactly_n_alphanumeric.match(input_text) is None:
            raise ValueError("Cipher does not contain " + str(CIPHER_LENGTH)
                + " characters or contains characters that are not lowercase "
                + "letters or numbers.")
        elif not self.__unique_characters(input_text):
            raise ValueError("Cipher containes non-unique characters")

        self.__cipher_text = input_text

    # This code is derived from https://stackoverflow.com/a/17357428/1873164
    # Sets only store unique characters, so if a set equals a string of chars,
    # it has unique characters
    def __unique_characters(self, text):
        """ Checks if characters in a string are unique.
        Args:
            text (str): The text to check for unique characters in.
        Return:
            True if the characters in the text are unique, False otherwise.
        """
        return len(set(text)) == len(text)

    def encode_decode_text(self, decoded_or_encoded_text):
        """Encode or Decode the decoded_or_encoded_text depending on the __encode_decode_mode.
        
        Args:
            decoded_or_encoded_text (EncodedText or DecodedText): The text to
                decode or encode.

        Returns:
            str: The encoded or decoded text.

        Raises:
            ValueError: If __encode_decode_mode or __cipher_text is not set.
        """
        if (not self.__cipher_text):
            raise ValueError("self.__cipher_text is not set.")
        
        result_char_list = []

        if self.__encode_decode_mode == EncodeDecodeMode.ENCODE:
            encoding_dict = {}

            for cipher_text_i, unicode_i in enumerate(range(97,123)):
                encoding_dict[chr(unicode_i)] = self.__cipher_text[cipher_text_i]
            
            for unicode_char in decoded_or_encoded_text.decoded_text:
                result_char_list.append(encoding_dict[str(unicode_char)])
        elif self.__encode_decode_mode == EncodeDecodeMode.DECODE:
            decoding_dict = {}

            for cipher_text_i, unicode_i in enumerate(range(97,123)):
                decoding_dict[self.__cipher_text[cipher_text_i]] = chr(unicode_i)
            
            for unicode_char in decoded_or_encoded_text.encoded_text:
                result_char_list.append(decoding_dict[str(unicode_char)])
        else:
            raise ValueError("self.__encode_decode_mode is not set.")

        return "".join(result_char_list)


CIPHER_LENGTH = MappingCipher.CIPHER_LENGTH
"""CIPHER_LENGTH (int): The length of the mapping cipher."""