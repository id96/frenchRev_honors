speeches_reader = open('raw_output/all_speeches.tsv', mode='r')
vocab_writer = open('clean_output/vocabulary.txt', mode='w')

# DONT READ ARCHIVES FROM SCRATCH AGAIN
# GO INTO TSV
# READ FROM TSV BY LINE
# CREATE A NEW TSV FROM THE ONE WE ALREADY DID 
for line in speeches_reader:
	line = line.rstrip().split('\t')
	raw_text = line[5]
	vocab_writer.write('{}\n'.format(raw_text))
	

#i have the header name here still 

speeches_reader.close()
vocab_writer.close()


