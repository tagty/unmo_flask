from random import choice
import re

class Responder:
    """docstring for [object Object]."""
    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary

    def response(self, *args):
        pass

    @property
    def name(self):
        return self._name


class WhatResponder(Responder):
    """docstring for [object Object]."""
    def response(self, text):
        return '{}ってなに？'.format(text)


class RandomResponder(Responder):
    """docstring for [object Object]."""
    def response(self, _):
        return choice(self._dictionary.random)


class PatternResponder(Responder):
    """docstring for [object Object]."""
    def response(self, text):
        for ptn in self._dictionary.pattern:
            matcher = re.match(ptn['pattern'], text)
            if matcher:
                chosen_response = choice(ptn['phrases'])
                return chosen_response.replace('%match%', matcher[0])
        return choice(self._dictionary.random)
