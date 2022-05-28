# Assigning Classes to Roles


## Classes

    a) CommandLineInterface
    b) MappingCipher
    c) DecodedText
    d) EncodedText
    e) EncryptionApp

## Assigning Classes to Roles

a)
* Get input
    1. Prompt for encode decode
    2. Enter text to encode/decode
    3. Enter cipher
* Order is optional but you need clear instructions

b)
* Validate cipher. 26 unique lowercase chars and digits 0-9.
* Use ValueError and handle it to re-enter the cipher.

c)
* Decoded Text
    * Remove punctuation, spaces, numbers - only letters are encoded/decoded
    * Text should be all lowercase letters with no spaces

d)
* Encoded Text
    * No specification in lab
    * Implied requirements
        * Should contain all cipher characters
        * For the best user experience, fail if not in the entire possible valid cipher text set, or get the cipher first and validate all characters in the cipher are in the encoded text.
        * To keep things simple I will just validate that the encoded text is lowercase alphanumeric and prompt the user to enter text that contains cipher characters.

b)
* Encode Decode Text
    * Decode the DecodedText
    * Encode the DecodedText

## Derived Roles
b)
* Manage the apps decode/encode mode

# Other requirements:

* At least 2 classes, and 3 user-defined functions (other than __init__() and main().
* At least 1 used iterable object.
* At least 1 used regular expression.
* Use naming conventions and formatting for code (variables, ClassNames, indentations).
* All Classes and functions need to contain docstring documentation.
* TAs will be our end user.