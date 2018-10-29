

from bs4 import BeautifulSoup
import os


# tomes = ['tome8.xml','tome9.xml', 'tome10.xml', 'tome11.xml', 'tome12.xml', 'tome13.xml', 'tome14.xml', 'tome15.xml', 'tome16.xml',
# 'tome17.xml', 'tome18.xml', 'tome19.xml', 'tome20.xml', 'tome21.xml', 'tome22.xml', 'tome23.xml', 'tome24.xml', 'tome25.xml', 
# 'tome26.xml', 'tome27.xml', 'tome28.xml', 'tome29.xml', 'tome30.xml', 'tome31.xml']

basepath = "archives/"
for filename in os.listdir(basepath):
	path = os.path.join(basepath, filename)
	with open(path, encoding="ISO-8859-1") as reader:
		soup = BeautifulSoup(reader, "lxml")
		tome = soup.find_all(type="volume")
		session = soup.find_all(type="session")
		date = soup.find_all("date")
		speeches = soup.find_all("sp")
		# speakers = soup.find_all("speaker")

		lines = []
		for x in speeches:
			# date = soup.find_all("date")
			speaker = soup.find("speaker")
			raw_text = soup.find_all("p") #need to concatenate these, use join? join only takes 1 parameter - 1 list with things inside
			line = "\t".join(speaker)
			lines.append(line)
		
		print(lines)






# for x in tomes:
# 	# with open("archives/%(x)a.xml") as fp:
# 	filename = "archives/{}".format(x)
# 	with open(filename, encoding="utf-8") as reader:
# 		soup = BeautifulSoup(reader, "lxml")
# 		# soup = BeautifulSoup(filename, 'lxml')
# 		# print(soup) #prints souped version of text
# 		# tag = soup.sp 
# 		# print(type(tag)) # returns <class 'bs4.element.Tag'>
# 		soup = soup.find_all('sp') #returns only speech tags
# 		# for x in enumerate(soup): #i is index, x is value
# 			# print(x) 


# 		# print(soup.prettify()) #prints pretty version of text
		



	



	




