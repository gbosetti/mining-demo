import re
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
# from Tokenizer import Tokenizer


class Tokenizer:

    # Tokenizing and with an identification of emoticons, mentions, hashtags, urls, etc
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""

    regex_str = [
        emoticons_str,
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)'  # anything else
    ]

    tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

    def tokenize(s, t):
        return s.tokens_re.findall(t)

    def preprocess(s, t, lowercase=False):
        tokens = s.tokenize(t)
        if lowercase:
            tokens = [token if s.emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens
