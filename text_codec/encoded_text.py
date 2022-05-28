"""Encoded Text Module
Author: Michael Metz
"""

import re

class EncodedText:
    """The encoded text that can be decoded. Any input text will be checked to
    see if they have alphanumeric characters as text can't be decoded if it
    contains characters that are not in the cipher.

    We could check encoded text against the cipher, but to still help the user
    without adding too much work, we can at least check that the encoded text
    is alphanumeric.

    Args:
        input_text (str): The text to get into EncodedText format.
    
    Attributes:
        encoded_text (str): The formatted text, ready for decoding.
    """

    encoded_text = ""

    def __init__(self, input_text):
        re_alphanumeric = re.compile("^[a-z0-9]+$")
        if re_alphanumeric.match(input_text) is None:
            raise ValueError("Encoded text does not contain lowercase alphanumeric characters.")
        
        self.encoded_text = input_text