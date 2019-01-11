import operator
import json
from collections import Counter
from Tokenizer import Tokenizer


class WordsCounter:

    tokenizer = Tokenizer()

    def count_most_common(self, file, num_terms):

        count_all = Counter()
        for line in file:
            tweet = json.loads(line)
            # Create a list with all the terms
            terms_all = [term for term in self.tokenizer.preprocess(tweet['text'])]
            # Update the counter
            count_all.update(terms_all)
        # Print the first 5 most frequent words
        return count_all.most_common(num_terms)


# Tokenizing
# tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# print(word_tokenize(tweet))  # With simple word tokenizing
# tokenizer = Tokenizer()
# print(tokenizer.preprocess(tweet))  #Including hasthags, urls, etc.
