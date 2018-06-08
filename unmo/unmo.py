from random import choice, randrange
from responder import WhatResponder, RandomResponder, PatternResponder, TemplateResponder
from dictionary import Dictionary
import morph

class Unmo:
    def __init__(self, name):
        self._dictionary = Dictionary()
        self._responders = {
            'what': WhatResponder('What', self._dictionary),
            'random': RandomResponder('Random', self._dictionary),
            'pattern': PatternResponder('Pattern', self._dictionary),
            'template': TemplateResponder('Template', self._dictionary)
        }
        self._name = name
        self._responder = self._responders['pattern']

    def dialogue(self, text):
        chance = randrange(0, 100)
        if chance in range(0, 39):
            self._responder = self._responders['pattern']
        elif chance in range(40, 69):
            self._responder = self._responders['template']
        elif chance in range(70, 89):
            self._responder = self._responders['random']
        else:
            self._responders = self._responders['what']

        parts = morph.analyze(text)
        response = self._responder.response(text, parts)
        self._dictionary.study(text, parts)
        return response

    def save(self):
        self._dictionary.save()

    def study(self, text, parts):
        self.study_random(text)
        self.study_pattern(text, parts)
        self.study_template(parts)

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name
