import urllib2
import sys
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

url = sys.argv[1]
with open(sys.argv[1], 'r') as f:
	for url in f:
		page = urllib2.urlopen(url)
		page = page.read()
		links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
		for link in links:
			if len(link[1]) > 1:
				print remove_tags(link[1])
