from collections import Counter

word_count = {}
for word in raw_text:
	word_count[word] += 1

print(word_count[:100])
print({key:value for key,value in word_count.items()[0:100]})

#use only top 100 words in this counter to make vocabulary, this will also help reduce word count