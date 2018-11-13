from bs4 import BeautifulSoup

session_writer = open ('raw_output/sessions_test.tsv', mode='w', encoding='utf-8')
session_writer.write("session_id\torganization\tpresident\tdate\n")

speeches_writer = open('raw_output/speeches_test_two.tsv', mode='w', encoding='utf-8')
speeches_writer.write("speech_id\tsession_id\tdate\tspeaker\traw_text\n")


tome_reader = open("archives/tome8.xml", encoding="utf-8")
soup = BeautifulSoup(tome_reader, "xml") # <class 'bs4.BeautifulSoup'>
# speeches = soup.find_all("sp") 
sessions = soup.find_all("div2", type="session")

	
speech_id = 0
session_id = 0 
for session in sessions:
	session_id += 1
	head_tags = session.find_all("head")
	organization = head_tags[0].text
	president = 'n/a'
#	for h in head_tags:
#		if h.text.lower().startswith('pr'):
#			president = h.text
#			break
	if len(head_tags) > 1:
		president = head_tags[1].text
	date = session.find("date")["value"] #reading the attribute value, green values are attributes
	session_writer.write('{}\t{}\t{}\t{}\n'.format(session_id, organization, president, date))

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

	
		speeches_writer.write('{}\t{}\t{}\t{}\t{}\n'.format(speech_id, session_id, date, speaker, raw_text))

session_writer.close()
speeches_writer.close() 
# for t in range(len(session)+1): #66 sessions in tome 8
# 		g.write(str(t))


