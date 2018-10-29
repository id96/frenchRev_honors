from bs4.diagnose import diagnose
with open("archives/tome8.xml") as fp:
	data = fp.read()
diagnose(data)