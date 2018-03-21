from random import choice

class Responder:
    """docstring for [object Object]."""
    def __init__(self, name):
        self._name = name

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

    RESPONSES = ['今日は寒いね', 'チョコ食べたい', 'きのう10円ひろった']

    def response(self, _):
        return choice(RandomResponder.RESPONSES)
