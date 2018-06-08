from random import choice
import re
import morph

class Responder:
    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary

    def response(self, *args):
        pass

    @property
    def name(self):
        return self._name


class WhatResponder(Responder):
    def response(self, text, _):
        return '{}ってなに？'.format(text)


class RandomResponder(Responder):
    def response(self, *args):
        return choice(self._dictionary.random)


class PatternResponder(Responder):
    def response(self, text, _):
        for ptn in self._dictionary.pattern:
            matcher = re.match(ptn['pattern'], text)
            if matcher:
                chosen_response = choice(ptn['phrases'])
                return chosen_response.replace('%match%', matcher[0])
        return choice(self._dictionary.random)

class TemplateResponder(Responder):
    def response(self, _, parts):
        keywords = [word for word, part in parts if morph.is_keyword(part)]
        count = len(keywords)
        if 0 < count:
            if count in self._dictionary.template:
                template = choice(self._dictionary.template[count])
                for keyword in keywords:
                    template = template.replace('%noun%', keyword, 1)
                return template
        return choice(self._dictionary.random)

