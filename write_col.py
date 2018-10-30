speeches_writer = open('raw_output/speeches_test.tsv', mode='w')

from bs4 import BeautifulSoup
with open("archives/tome8.xml", encoding="utf-8") as reader: 
		soup = BeautifulSoup(reader, "lxml") # <class 'bs4.BeautifulSoup'>
		# speeches = soup.find_all("sp") 
		sessions = soup.find_all(type="session")
		
		
with speeches_writer as g:
	# writer = csv.writer(g, delimiter = '\t') #writing to tsv
	# g.writerow("speech_id", "num_tome", "session_id", "speaker", "raw_text")
	
	# writer.writerow(["speech_id\tsession_id\tspeaker\traw_text"])
	
	g.write("speech_id\tsession_id\tspeaker\traw_text\n")
	speech_id = 0
	session_id = 0 
	for session in sessions:
		session_id += 1
		speeches = session.find_all("sp")
		for speech in speeches:
			speech_id += 1
			speaker = speech.find("speaker").text
			p = speech.find_all("p")
			para_texts = [para.text for para in p]
			raw_text = ' '.join(para_texts)
			raw_text = raw_text.replace('\t', ' ')
			lines = raw_text.split()
			raw_text = ' '.join(lines)






		# g.write(str(speech_id)+'\t'+str(session_id)+'\t'+str(speaker)+'\t'+str(raw_text))
		# g.write(str(speech_id)+'\t'+str(speaker)+'\t'+'\n')
			g.write('\t'.join([str(speech_id), str(session_id), speaker, raw_text]) + '\n')





	
	# for t in range(len(session)+1): #66 sessions in tome 8
	# 		g.write(str(t))

