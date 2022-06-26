__author__ = 'Deza Farras Tsany<deza.ftsany@gmail.com>'
__version__ = '1.0.0'

"""
This module offers random password generation.
"""

from random import choice, randint, shuffle
from string import digits, punctuation, ascii_letters

_min_length = 5
_max_length = 8
_min_digit_length = 7
_max_digit_length = 12
_min_word_length = 9
_max_word_length = 15

def _randomDigits():
    length = randint(_min_length, _max_length)
    return ''.join(choice(digits) for i in range(length))

def _randomPunctuation():
    length = randint(_min_digit_length, _max_digit_length)
    return ''.join(choice(punctuation) for i in range(length))

def _randomWord():
    length = randint(_min_word_length, _max_word_length)
    return ''.join(choice(ascii_letters) for i in range(length))

def generate():
    """
    This function aims to generate passwords randomly
    """
    str_pass = _randomDigits() + _randomPunctuation() + _randomWord()
    str_pass = list(str_pass)
    shuffle(str_pass)
    return ''.join( str_pass )