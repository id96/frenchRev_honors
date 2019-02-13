import re, sys, random, math
import numpy as np
from collections import Counter

# word_pattern = re.compile("\w[\w\-\']*\w|\w")



if len(sys.argv) != 3:
    print("Usage: topicmodel.py [docs file] [num topics]")
    sys.exit()

num_topics = int(sys.argv[2])
# doc_smoothing = 0.5
# word_smoothing = 0.01

# stoplist = set()
# with open("stoplist.txt", encoding="utf-8") as stop_reader:
#     for line in stop_reader:
#         line = line.rstrip()
#         stoplist.add(line)

word_counts = Counter()

documents = []
word_topics = {}
topic_totals = np.zeros(num_topics)

# for line in open(sys.argv[1], encoding="utf-8"):
    #line = line.lower()
    
    # tokens = word_pattern.findall(line)
    
    # ## remove stopwords, short words, and upper-cased words
    # tokens = [w for w in tokens if not w in stoplist and len(w) >= 3 and not w[0].isupper()]
    # word_counts.update(tokens)
    
doc_topic_counts = np.zeros(num_topics)
token_topics = []

vocab_reader = open('clean_output/reduction_test.txt', mode='r')

for line in vocab_reader:
    for word in line:
    ## Generate a topic randomly
        topic = random.randrange(num_topics)
        token_topics.append({ "word": word, "topic": topic })
    
    ## If we haven't seen this word before, initialize it
        if not word in word_topics:
            word_topics[word] = np.zeros(num_topics)
    
    ## Update counts: 
        word_topics[word][topic] += 1
        topic_totals[topic] += 1
        doc_topic_counts[topic] += 1

    documents.append({ "original": line, "token_topics": token_topics, "topic_counts": doc_topic_counts })

## Now that we're done reading from disk, we can count the total
##  number of words.
vocabulary = list(word_counts.keys())
vocabulary_size = len(vocabulary)

def print_topic(topic):
    sorted_words = sorted(vocabulary, key=lambda w: word_topics[w][topic], reverse=True)
    
    for i in range(20):
        w = sorted_words[i]
        print("{}\t{}".format(word_topics[w][topic], w))

def print_all_topics():
    for topic in range(num_topics):
        sorted_words = sorted(vocabulary, key=lambda w: word_topics[w][topic], reverse=True)
        print(" ".join(sorted_words[:20]))