import json
from WordsCounter import WordsCounter


file_name = 'data/stream_lyon.json'

# Reading the full dataset
with open(file_name, 'r') as file:
    # line = file.readline()  # read only the first tweet/line
    # tweet = json.loads(line)  # load it as Python dict

    # Tokenizing and word counting
    words_counter = WordsCounter()
    print(words_counter.count_most_common(file, 5))



