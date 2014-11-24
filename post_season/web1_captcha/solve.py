# Majority of this code is from: http://www.boyter.org/decoding-captchas/

# This code was created for the NCL 2014 Post Season Game: Web 1.  Where you needed to
# enter the captcha phrase (case sensitive) 10,000 times consecutively.  A wrong guess
# set the counter back to zero.  Due to it being a timed event, the code is very very
# sloppy.  I thought about cleaning it up and may do that some day but figured seeing
# bad code has its benefits.

# The captcha image had a few flaws which made it easy to break.
## It used a single color exclusively for the character.  That meant we could search
### the canvis for that color and output it to a new canvis and unobstruct the image.
## Characters did not overlap.  This made it trivial to cut the image up into pieces
### that only contained a single character, making it easy for OCR.

# Usage
# This assumes you have already built a dictionary by placing the images of each 
# letter into the appropriate folder in iconset.  This set already exists
# if you are using it for the NCL Web Challenge 1.  Everything (URL, User, Pass) 
# hard coded so just execute the script.

from PIL import Image
import time
import hashlib
import time
import os
import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup


import math

# Vector space magic.
class VectorCompare:
  def magnitude(self,concordance):
    total = 0
    for word,count in concordance.iteritems():
      total += count ** 2
    return math.sqrt(total)

  def relation(self,concordance1, concordance2):
    relevance = 0
    topvalue = 0
    for word, count in concordance1.iteritems():
      if concordance2.has_key(word):
        topvalue += count * concordance2[word]
    return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))

def buildvector(im):
  d1 = {}

  count = 0
  for i in im.getdata():
    d1[count] = i
    count += 1

  return d1

## Start of program.

# Load 'dictionary'
v = VectorCompare()

iconset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']

imageset = []

for letter in iconset:
  for img in os.listdir('./iconset/%s/'%(letter)):
    temp = []
    if img != "Thumbs.db": # windows check...
      temp.append(buildvector(Image.open("./iconset/%s/%s"%(letter,img))))
    imageset.append({letter:temp})


# Initialize Web Browser
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# LOGIN PAGE
ncl = br.open('https://23.23.158.181/index.php')
html = ncl.read()

# Log into the page with super secure credentials.
br.select_form(nr=0)
br.form['username'] = 'ipp'
br.form['password'] = 'test'

ncl = br.submit()
html = ncl.read()


# Horrible loop.  In hindsight, should of atleast put a counter in to stop after 4
# consecutive failures.  Essentially, we go to the captcha page download, analyze,
# and submit the captcha unless we are at try 9,999.  After that the break can be moved
# outside the if statement and a print html can be inserted to dump the page.  This was
# the safest method to not go above 10,000 tries since it may reset.
while 1:
	# Ran into an occasional error within retrieving the html page.  Don't care to
	# do more debuging than I need to.  So lets just retry that unless it happens
	# 4x consecutively (I don't believe this portion of code worked).
	for i in range(0,3):
 	 while True:	
	  try:
	    # Get the "main" page.  Contains captcha and submit form.
 	    br.open('https://23.23.158.181/main.php')
	    # Get the captcha and save to a file.  Could of done this all from memory
	    # but this was just easier for debugging failures.
	    captcha = br.open_novisit('https://23.23.158.181/captcha.png')
	    with open ('captcha.png','wb') as f:
	      f.write(captcha.read())
	  except:
            print "ERROR Attempting to Recover. HTTP GET"
	    continue
	  break

	# Begin of analyzing.  Open the image.
	im = Image.open("captcha.png")
	im2 = Image.new("P",im.size,255)
	im = im.convert("P")
	temp = {}

	# Create unabstructed canvas with characters on it.  If black pixle move to new.
	for x in range(im.size[1]):
	  for y in range(im.size[0]):
	    pix = im.getpixel((y,x))
	    temp[pix] = pix
	    if pix == 0: # these are the numbers to get
	      im2.putpixel((y,x),0)

    	# Clean some variables
	inletter = False
	foundletter=False
	start = 0
	end = 0

	letters = []

	# Slice the captcha into individual characters.
	for y in range(im2.size[0]): # slice across
	  for x in range(im2.size[1]): # slice down
	    pix = im2.getpixel((y,x))
	    if pix != 255:
	      inletter = True

	  if foundletter == False and inletter == True:
	    foundletter = True
	    start = y

	  if foundletter == True and inletter == False:
	    foundletter = False
	    end = y
	    letters.append((start,end))


	  inletter=False

	# Magical OCR piece.
	answer = ""
	count = 0
	for letter in letters:
	  m = hashlib.md5()
	  im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))

	  guess = []

	  for image in imageset:
	    for x,y in image.iteritems():
	      if len(y) != 0:
	        guess.append( ( v.relation(y[0],buildvector(im3)),x) )

	  guess.sort(reverse=True)
#	  print guess[0]
	  answer = answer+guess[0][1]
	  count += 1

	# Have our answer.  Lets fill out the form and submit.
	br.select_form(nr=0)
	br.form['input']=answer
	ncl = br.submit()
	html = ncl.read()
	html_soup = BeautifulSoup(html)
	h1 = html_soup.find('h1')
	if "9999" in str(h1):
	  print h1
	  break
	if "failed" in str(h1):
	  print h1
	  print answer
        print "%s - %s" % (answer,h1)
