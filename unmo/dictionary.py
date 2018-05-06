import re
from janome.tokenizer import Tokenizer

class Dictionary:
    """docstring for [object Object]."""

    DICT_RANDOM = 'unmo/dics/random.txt'
    DICT_PATTERN = 'unmo/dics/pattern.txt'
    TOKENIZER = Tokenizer()

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

    def study(self, text):
        self.study_random(text)

    def study_random(self, text):
        if not text in self._random:
            self._random.append(text)

    def study_pattern(self, text, parts):
        for word, part in parts:
            if self.is_keyword(part):
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                if duplicated:
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                else:
                    self._pattern.append({'pattern': word, 'phrases': [text]})

    def save(self):
        with open(Dictionary.DICT_RANDOM, mode='w', encoding='utf-8') as f:
            f.write('\n'.join(self.random))

    @staticmethod
    def analyze(text):
        return [(t.surface, t.part_of_speech) for t in Dictionary.TOKENIZER.tokenize(text)]

    @staticmethod
    def pattern_to_line(pattern):
        return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

    @staticmethod
    def is_keyword(part):
        return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)', part))
