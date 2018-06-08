import os.path
from collections import defaultdict
import morph

class Dictionary:
    DICT = { 
            'random': 'unmo/dics/random.txt',
            'pattern': 'unmo/dics/pattern.txt',
            'template': 'unmo/dics/template.txt',
            }


    def __init__(self):
        with open(Dictionary.DICT['random'], encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        with open(Dictionary.DICT['pattern'], encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

        with open(Dictionary.DICT['template'], encoding='utf-8') as f:
            self._template = defaultdict(lambda: [], {})
            for line in f:
                count, template = line.strip().split('\t')
                if count and template:
                    count = int(count)
                    self._template[count].append(template)

    @staticmethod
    def touch_dics():
        for dic in Dictionary.DICT.values():
            if not os.path.exists(dic):
                open(dic, 'w').close()

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

    @property
    def template(self):
        return self._template

    def study(self, text, parts):
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

    def study_template(self, parts):
        template = ''
        count = 0
        for word, part in parts:
            if morph.is_keyword(part):
                word = '%noun%'
                count += 1
            template += word

        if 0 < count and template not in self._template[count]:
            self._template[count].append(template)

    def save(self):
        with open(Dictionary.DICT['random'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join(self.random))

        with open(Dictionary.DICT['pattern'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join([Dictionary.pattern_to_line(p) for p in self._pattern]))

        with open(Dictionary.DICT['template'], mode='w', encoding='utf-8') as f:
            for count, templates in self.template.items():
                for template in templates:
                    f.write('{}\t{}\n'.format(count, template))

    @staticmethod
    def pattern_to_line(pattern):
        return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

