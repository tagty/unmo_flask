import re
from janome.tokenizer import Tokenizer

TOKENIZER = Tokenizer()

def analyze(text):
    return [(t.surface, t.part_of_speech) for t in TOKENIZER.tokenize(text)]

def is_keyword(part):
    return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)', part))

