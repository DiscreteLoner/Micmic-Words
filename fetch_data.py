"""
fetch_data module
December 8, 2018
"""
def fetch_web_data(source):
	from bs4 import BeautifulSoup
	import urllib2

	req = urllib2.Request(source)
	response = urllib2.urlopen(req)

	text = response.read()

	response.close()

	text = BeautifulSoup(text, "html.parser").get_text(strip = True)
	return text