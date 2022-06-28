__author__ = 'Deza Farras Tsany<deza.ftsany@gmail.com>'
__version__ = '1.0.0'

"""
This module offers random password generation.
"""

from random import choice, randint, shuffle
from string import digits, punctuation, ascii_letters
from .check import check

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



class generate():

    def __init__(self) :
        pass

    def __response(self, password='', level=0, strength='', message='') :
        return {
            'password': password,
            'level': level,
            'strength': strength,
            'message': message
        }

    def number(self, min=6, max=6) :
        length = randint(min, max)
        str_pass = ''.join(choice(digits) for i in range(length))
        checkPassword = check(str_pass)
        return self.__response(str_pass, level=checkPassword['level'], strength=checkPassword['strength'], message=checkPassword['message']) 

    def __punctuation(self, min=6, max=6) :
        length = randint(min, max)
        str_pass = ''.join(choice(punctuation) for i in range(length))
        checkPassword = check(str_pass)
        return self.__response(str_pass, level=checkPassword['level'], strength=checkPassword['strength'], message=checkPassword['message']) 
    
    def letter(self, min=6, max=6) :
        length = randint(min, max)
        str_pass = ''.join(choice(ascii_letters) for i in range(length))
        checkPassword = check(str_pass)
        return self.__response(str_pass, level=checkPassword['level'], strength=checkPassword['strength'], message=checkPassword['message'])
    
    def numberLetter(self):
        pass_number = self.number(min=3, max=5)
        pass_letter = self.letter(min=3, max=5)
        
        str_pass = pass_number['password'] +  pass_letter['password']
        str_pass = list(str_pass)
        shuffle(str_pass)
        str_pass = ''.join( str_pass )

        checkPassword = check(str_pass)
        
        return self.__response(str_pass, level=checkPassword['level'], strength=checkPassword['strength'], message=checkPassword['message'])

    def random(self) :
        """
            This function aims to generate passwords randomly
        """
        pass_number = self.number(_min_digit_length, _max_digit_length)
        pass_punctuation = self.__punctuation(_min_length, _max_length)
        pass_letter = self.letter(_min_word_length, _max_word_length)
        
        str_pass = pass_number['password'] + pass_punctuation['password'] + pass_letter['password']
        str_pass = list(str_pass)
        shuffle(str_pass)
        str_pass = ''.join( str_pass )

        checkPassword = check(str_pass)
        
        return self.__response(str_pass, level=checkPassword['level'], strength=checkPassword['strength'], message=checkPassword['message'])