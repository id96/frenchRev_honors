from bs4 import BeautifulSoup
import os 


speeches_writer = open('raw_output/all_speeches.tsv', mode='w')
speeches_writer.write("tome\tspeech_id\tsession_id\tdate\tspeaker\traw_text\n")


basepath = "archives/"
for filename in os.listdir(basepath):
	if not filename.endswith('.xml'):
		continue
	print('Reading {}...'.format(filename))
	path = os.path.join(basepath, filename)

	reader = open(path, encoding="utf-8-sig")
	soup = BeautifulSoup(reader, "xml") # <class 'bs4.BeautifulSoup'>
	sessions = soup.find_all("div2", type="session")

	if len(filename) == 9:
		tome = filename[4]
	if len(filename) == 10:
		tome = filename[4:6]
	
	speech_id = 0
	session_id = 0 
	for session in sessions:
		session_id += 1
		date = session.find("date")["value"]
		speeches = session.find_all("sp")
		for speech in speeches:
			speech_id += 1
			speaker_tag = speech.find("speaker")
			if speaker_tag:
				speaker = speaker_tag.text
				speaker = speaker.replace('\n', ' ')
			else:
				speaker = 'n/a'
			p = speech.find_all("p")
			para_texts = [para.text for para in p]
			raw_text = ' '.join(para_texts)
			raw_text = raw_text.replace('\t', ' ')
			raw_text = raw_text.replace('\n', ' ')
			lines = raw_text.split()
			raw_text = ' '.join(lines)

			speeches_writer.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(tome, speech_id, session_id, date, speaker, raw_text))

speeches_writer.close() 



