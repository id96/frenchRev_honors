# sessions.tsv

# give ids to every session to keep track of them

# columns
# 1. id
# 2. tome
# 3. header 1
# 4. header 2
# 5. date
# 6. num of speeches in session

# 	id 	tome	head (what was in session)	head (president)	date	num of speeches in session
# session 1
# session 2
# session 3
# .
# .
# .


# speeches.tsv

# columns 
# 1. id
# 2. tome
# 3. 
# 4. 
# 5. 
# 	id tome session_id 	speaker	raw text(concatonated paragraphs)

import csv
sessions_writer = open('raw_output/sessions.tsv', mode="w") 
speeches_writer = open('raw_output/speeches.tsv', mode='w')

from bs4 import BeautifulSoup
with open("archives/tome8.xml", encoding="utf-8") as reader: 
		soup = BeautifulSoup(reader, "lxml") # <class 'bs4.BeautifulSoup'>
		speeches = soup.find_all("sp") 
		session = soup.find_all(type="session")
		paragraphs = soup.find_all("p") #22034 paragraphs total
		raw_text = []
		for speech in speeches:
			p = speech.find_all("p") #type result set
			for x in p:
				raw_text.append(x.text)
		# print(len(session))
		# print(len(raw_text)) #12696, this makes sense intuitevly because there are p tags not nested in sp tags
		# tome = soup.find_all(type="volume")
		

with speeches_writer as g:
	writer = csv.writer(g, delimiter = '\t') #writing to tsv
	# g.writerow("speech_id", "num_tome", "session_id", "speaker", "raw_text")
	writer.writerow(["id"])
	for i in range(len(speeches)+1): #1964 speeches in tome 8
			g.write(str(i))
			# g.write(str(tome[i]))
	writer.writerow(["tome"])
	writer.writerow(["session id"])
	for t in range(len(session)+1): #66 sessions in tome 8
			g.write(str(t))
			# g.write(str(tome[i]))
	writer.writerow(["speaker"])
	for u in speeches:
		speaker = u.find("speaker").text
		g.write(str(speaker)+'\t')
	writer.writerow(["raw text"])

	#for speech in speeches:
		# line = ''
		# concatenate id to line
		#  concatenate tome to line
		# concatenate session id to line
		# concatenate speaker to line
		# concatenate raw text to line
	



with sessions_writer as f:
	writer = csv.writer(f, delimiter = '\t') #writing to tsv
	writer.writerow(["id"])
	writer.writerow(["tome"])
	writer.writerow(["header 1"])
	writer.writerow(["header 2"])
	writer.writerow(["date"])
	writer.writerow(["num speeches"])
	f.write("hello world")
