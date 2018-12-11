from bs4 import BeautifulSoup
import os 


speeches_writer = open('raw_output/num_sp.tsv', mode='w')
speeches_writer.write("tome\ttome_num_speech\n")

archive_total = 0
basepath = "archives/"
for filename in os.listdir(basepath):
	if not filename.endswith('.xml'):
		continue
	#print('Reading {}...'.format(filename))
	path = os.path.join(basepath, filename)

	reader = open(path, encoding="utf-8-sig")
	soup = BeautifulSoup(reader, "xml") # <class 'bs4.BeautifulSoup'>
	sessions = soup.find_all("div2", type="session")

	if len(filename) == 9:
		tome = filename[4]
	if len(filename) == 10:
		tome = filename[4:6]
	
	tome_total = 0
	for session in sessions:
		speeches = session.find_all("sp", recursive=False)
		num_speeches = len(speeches)
		tome_total += num_speeches
	#print(tome_total)
	speeches_writer.write('{}\t{}\n'.format(tome, tome_total))
	
	archive_total += tome_total
#print(archive_total)
speeches_writer.close() 