vocab_reader = open('clean_output/reduction_test.txt', mode='r')


# for word in vocab_reader:
#     lines = word.split()

total = 0
for line in vocab_reader:
    total += len(line)

# word_total = len(lines)
# print(word_total)
print(total)
#5679953 words total with cleaned vocab
#1 million extra words