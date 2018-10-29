# text.lower

# if len(word) < 3:
# 	remove word

# text cleaning is not manual

# need to document what im fixing

# space separated tokens (fully tokenize)

# if list of strings
# " ".join(list) - concatenates in one string, acting as a delimiter

import re, sys
word_pattern = re.compile("[\w-]+")

tomes = ['tome8.xml','tome9.xml', 'tome10.xml', 'tome11.xml', 'tome12.xml', 'tome13.xml', 'tome14.xml', 'tome15.xml', 'tome16.xml',
'tome17.xml', 'tome18.xml', 'tome19.xml', 'tome20.xml', 'tome21.xml', 'tome22.xml', 'tome23.xml', 'tome24.xml', 'tome25.xml', 
'tome26.xml', 'tome27.xml', 'tome28.xml', 'tome29.xml', 'tome30.xml', 'tome31.xml']


for x in tomes:
	# with open("archives/%(x)a.xml") as fp:
	filename = "archives/{}".format(x)
	with open(filename, encoding="utf-8") as reader:
		for line in reader:
        line = line.rstrip()
        
        ## This converts a string (line) into a list (tokens)
        tokens = word_pattern.findall(line)
        
        print(tokens)
