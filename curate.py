import re, sys 
import numpy as np 
from collections import Counter

word_pattern = re.compile("\w[\-\w]+\w")


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

#separate and then drop

#print (zip(*[line.split() for line in speeches_reader])[1])

#final = []
counter = Counter()
for line in vocab_reader:
	line = line.rstrip() #removes trailing characters
	line = line.lower()	#makes lowercase
	tokens = word_pattern.findall(line)
	for word in tokens: # tokens = ' '.join(tokens) #should i join? joining items in a list into a string 
		if word not in stopwords:
			#separate
			#if len(word) > 3:
				#final.append(word)
			counter[word] += 1 #if i get rid of final array
#counter.update(final) # counter.update(tokens)
#print(counter)

#most_common function for counter for top 10,000
most_common = counter.most_common(10000)
vocabulary = [word for word, count in most_common]
#print(vocabulary)
total_words = sum([count for word, count in most_common])
print(total_words)


# word_count = {}
# for word in raw_text:
# 	word_count[word] += 1

# print(word_count[:100])
# print({key:value for key,value in word_count.items()[0:100]})

#vocab_writer.write(vocabulary)
vocab_reader.close()
vocab_writer.close() 