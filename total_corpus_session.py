from bs4 import BeautifulSoup
import os 

session_writer = open ('raw_output/all_sessions.tsv', mode='w')
session_writer.write("tome\tsession_id\torganization\tpresident\tdate\n")

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
		session_writer.write('{}\t{}\t{}\t{}\t{}\n'.format(tome, session_id, organization, president, date))

session_writer.close()