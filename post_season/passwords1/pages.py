import urllib2
import sys
import re

TAG_RE = re.compile(r'<[^>]+>')
PAGE_RE = re.compile(r'^/')

def remove_tags(text):
    return TAG_RE.sub('', text)

url = sys.argv[1]
page = urllib2.urlopen(url)
page = page.read()
links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
for link in links:
    if re.match(r'/', link[0]):
	    print 'http://www.wowwiki.com%s' % (link[0])
