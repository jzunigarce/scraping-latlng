import sys
import urllib
import re
from bs4 import BeautifulSoup

if len(sys.argv) >= 2:
	url = sys.argv[1]
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	text = soup.find_all('aside', attrs={ 'class': "widget widget_srmgmap_widget"})
	print text
	latlng = re.findall(r"\d+\.\d+,-*\d+\.\d+", str(text[0]))
	print latlng
	if len(latlng) > 0:
		print(latlng[0])
	else:
		print 'Not found latlng'
else:
	print "Formato incorrecto"