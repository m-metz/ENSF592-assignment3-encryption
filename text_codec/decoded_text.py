"""Decoded Text Module
Author: Michael Metz
"""

import re

class DecodedText:
    """The decoded text that can be encoded. Any input text will be lower cased
    and have non-alphanumeric characters removed.

    Args:
        input_text (str): The text to get into DecodedText format.
    
    Attributes:
        decoded_text (str): The formatted text, ready for encoding.
    """
    decoded_text = ""

    def __init__(self, input_text):
        input_text = input_text.lower()
        
        # Remove non-alphanumeric characters
        # Obtained from https://stackoverflow.com/a/5843547/1873164
        input_text = re.sub('[^A-Za-z]+', '', input_text)
        
        self.decoded_text = input_text