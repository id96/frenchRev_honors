import re, sys 
import numpy as np 
from collections import Counter

word_pattern = re.compile("\w[\-\w]+\w")


vocab_reader = open('clean_output/reduction_test.txt', mode='r')
vocab_writer = open('clean_output/reduction_test_string2.txt', mode='w')
stopwords = ['les', 'que', 'des', 'qui', 'est', 'vous', 'dans', 'pour', 'une',
			 'pas', 'par', 'sur', 'nous', 'cette', 'aux', 'mais', 'ils', 'leur',
			 'être', 'sont', 'ces', 'ont', 'elle', 'tous', 'avec', 'faire', 'son',
			 'ses', 'dont', 'comme', 'votre', 'soit', 'lui', 'peut', 'leurs', 'donc',
			 'avez', 'doit', 'faut', 'sera', 'était', 'vos', 'ceux', 'avoir', 'cet', 'nos', 'ainsi', 'avait']

# final = []
# counter = Counter()

for line in vocab_reader:
	# line = line.rstrip() 
	# line = line.lower()	
	# tokens = word_pattern.findall(line)
	# for word in tokens:
	# 	if word in stopwords:
	# 		word = word.replace(word,'')
	#join the words in tokens .join(' ')
	text = ' '.split(line)
	vocab_writer.write('{}\n'.format(text))
	# vocab_writer.write('{}\n'.format(tokens))
	# print(tokens)

vocab_reader.close()
vocab_writer.close() 