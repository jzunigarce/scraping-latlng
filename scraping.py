import sys
import urllib
import re
from bs4 import BeautifulSoup

if len(sys.argv) >= 2:
	url = sys.argv[1]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	result = soup.find_all('aside', attrs={ 'class': "widget widget_srmgmap_widget"})
	text = ''
	for tag in result:
		text += tag.getText()

	latlng = re.findall(r"\d+\.\d+,\s?-?\d+\.\d+", text)

	if len(latlng) > 0:
		print(latlng[0])
	else:
		print 'Not found latlng'
else:
	print "Formato incorrecto"