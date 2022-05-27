"""Decoded Text Module
Author: Michael Metz
"""

import re

class DecodedText:
    
    decoded_text = ""

    def __init__(self, input_text):
        re_alphanumeric = re.compile("^[a-z0-9]+$")
        input_text = input_text.lower()
        
        # Remove non-alphanumeric characters
        # Obtained from https://stackoverflow.com/a/5843547/1873164
        input_text = re.sub('[^A-Za-z0-9]+', '', input_text)
        
        self.decoded_text = input_text