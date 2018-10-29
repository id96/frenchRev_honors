from bs4 import BeautifulSoup

# not ISO-8859-1
with open("archives/tome8.xml", encoding="utf-8") as reader: 

		soup = BeautifulSoup(reader, "lxml") # <class 'bs4.BeautifulSoup'>
		# print(soup.text)

		# tome = soup.find_all(type="volume")
		# session = soup.find_all(type="session")
		# date = soup.find_all("date")
		speeches = soup.find_all("sp") 
		# print(len(speeches)) #1964
		# print(type(speeches)) = <class 'bs4.element.ResultSet'>
			# print(speeches)
		# speakers = soup.find_all("speaker")


		# Find all speakers in tome
		speakers = []
		for x in speeches:
			speaker = x.find("speaker")
			speakers.append(speaker)
			# line = "\t".join(speakers.text)
			# print(line)
		print(speakers)
		print(len(speakers)) #1964

	





			# raw_text = soup.find_all("p") #need to concatenate these, use join? join only takes 1 parameter - 1 list with things inside
		
