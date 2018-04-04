class Dictionary:
    """docstring for [object Object]."""

    DICT_RANDOM = 'unmo/dics/random.txt'
    DICT_PATTERN = 'unmo/dics/pattern.txt'

    def __init__(self):
        with open(Dictionary.DICT_RANDOM, encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        with open(Dictionary.DICT_PATTERN, encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

    @staticmethod
    def make_pattern(line):
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            return {'pattern': pattern, 'phrases': phrases.split('|')}

    @property
    def random(self):
        return self._random

    @property
    def pattern(self):
        return self._pattern
