from responder import RandomResponder


class Unmo:
    """docstring for [object Object]."""
    def __init__(self, name):
        self._name = name
        self._responder = RandomResponder('Random')

    def dialogue(self, text):
        return self._responder.response(text)

    @property
    def name(self):
        return self._name

    @property
    def responder_name(self):
        return self._responder.name
