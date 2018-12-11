import re, sys 
import numpy as np 
from collections import Counter

word_pattern = re.compile("\w[\w\-\']*\w|\w")
tome_counts = {}
word_counts = Counter()

vocab_reader = open('clean_output/vocabulary.txt', mode='r')
vocab_writer = open('clean_output/reduction_test.txt', mode='w')
stopwords = ['les', 'que', 'des', 'qui', 'est', 'vous', 'dans', 'pour', 'une',
			 'pas', 'par', 'sur', 'nous', 'cette', 'aux', 'mais', 'ils', 'leur',
			 'être', 'sont', 'ces', 'ont', 'elle', 'tous', 'avec', 'faire', 'son',
			 'ses', 'dont', 'comme', 'votre', 'soit', 'lui', 'peut', 'leurs', 'donc',
			 'avez', 'doit', 'faut', 'sera', 'était', 'vos', 'ceux', 'avoir', 'cet', 'nos', 'ainsi', 'avait']

#make lowercase, remove words less than 3 letters, remove word if in stopwords list,
#seperate contractions
#write only top 10,000 words

#print (zip(*[line.split() for line in speeches_reader])[1])

final = []
counter = Counter()
for line in vocab_reader:
	line = line.rstrip() #removes trailing characters
	line = line.lower()	#makes lowercase
	tokens = word_pattern.findall(line)
	for word in tokens: # tokens = ' '.join(tokens) #should i join? joining items in a list into a string 
		if word not in stopwords:
			if len(word) > 3:
				final.append(word)
	counter.update(final) # counter.update(tokens)
	#print(counter)

word_counts.update(counter)
vocabulary = list(word_counts.keys())

#print(len(vocabulary))


# word_count = {}
# for word in raw_text:
# 	word_count[word] += 1

# print(word_count[:100])
# print({key:value for key,value in word_count.items()[0:100]})

#vocab_writer.write(vocabulary)
vocab_reader.close()
vocab_writer.close() 