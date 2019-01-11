import re
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
import string
import operator
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


class Tokenizer:

    punctuation = list(string.punctuation)
    stop_words = stopwords.words('english') + punctuation + ['rt', 'via']

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

    def remove_stopwords(self, tweet):
        return [term for term in self.preprocess(tweet['text']) if term not in self.stop_words]

    def tokenize(s, t):
        return s.tokens_re.findall(t)

    def preprocess(s, t, lowercase=False):
        tokens = s.tokenize(t)
        if lowercase:
            tokens = [token if s.emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    def common_terms(self, tweets, num_terms=None):

        count_all = Counter()
        for tweet in tweets:
            # Create a list with all the terms
            tokens = self.remove_stopwords(tweet)
            # Update the counter
            count_all.update(tokens)

        # Print the first n most frequent words
        return count_all.most_common(num_terms)

    def filterMentions(self, term):

        if term.startswith('@'):
            return True
        else:
            return False

    def common_mentions(self, tweets, num_terms=None):

        count_all = Counter()
        for tweet in tweets:
            tokens = self.remove_stopwords(tweet)
            # hashtags = [for term in tokens: if term.startswith('#') return true ]

            mentions = filter(lambda token: token.startswith('@'), tokens)

            count_all.update(mentions)
        return count_all.most_common(num_terms)
