from random import choice, randrange
from responder import WhatResponder, RandomResponder, PatternResponder
from dictionary import Dictionary


class Unmo:
    """docstring for [object Object]."""
    def __init__(self, name):
        self._dictionary = Dictionary()
        self._responders = {
            'what': WhatResponder('What', self._dictionary),
            'random': RandomResponder('Random', self._dictionary),
            'pattern': PatternResponder('Pattern', self._dictionary)
        }
        self._name = name
        self._responder = self._responders['pattern']

    def dialogue(self, text):
        chance = randrange(0, 100)
        if chance in range(0, 59):
            self._responder = self._responders['pattern']
        elif chance in range(60, 89):
            self._responder = self._responders['random']
        else:
            self._responders = self._responders['what']

        response = self._responder.response(text)
        self._dictionary.study(text)
        return response

    def save(self):
        self._dictionary.save()

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name
