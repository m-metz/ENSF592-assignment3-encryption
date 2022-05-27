"""Encoded Text Module
Author: Michael Metz
"""

import re

class EncodedText:
    
    encoded_text = ""

    def __init__(self, input_text):
        re_alphanumeric = re.compile("^[a-z0-9]+$")
        if re_alphanumeric.match(input_text) is None:
            raise ValueError("Encoded text does not contain alphanumeric characters.")
        
        self.encoded_text = input_text