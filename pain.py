vocab_reader = open('raw_output/all_speeches.tsv', mode='r')

oct_words = []
count = 0
for line in vocab_reader:
	# print(line)

	if "1789-10-05" in line:
		count += 1
		# print(line)

print(count) #49 speeches on 10/05/1789
vocab_reader.close()