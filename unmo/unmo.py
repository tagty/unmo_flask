from random import choice
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
        chosen_key = choice(list(self._responders.keys()))
        self._responder = self._responders[chosen_key]
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name
