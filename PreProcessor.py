import json
from Tokenizer import Tokenizer


class PreProcessor:

    def __init__(self):
         self.tokenizer = Tokenizer()

    def read_raw_tweets(self, file_name):

        tweets = []
        with open(file_name, 'r') as file:
            for line in file:
                tweet = json.loads(line)
                tweets.append(tweet)

        return tweets

    def common_terms(self, tweets, max_terms):

        return self.tokenizer.common_terms(tweets, max_terms)

    def common_mentions(self, tweets, max_terms):

        return self.tokenizer.common_mentions(tweets, max_terms)


# Instantiating the pre-processor and analyzing the data
preprocessor = PreProcessor()
tweets = preprocessor.read_raw_tweets('data/stream_lyon.json')

print("Most common tokens: ", preprocessor.common_terms(tweets, 5))
print("Most common mentions: ", preprocessor.common_mentions(tweets, None))