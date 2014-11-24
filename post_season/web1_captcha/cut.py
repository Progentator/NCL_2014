# Majority of this code is from: http://www.boyter.org/decoding-captchas/

# This code was created for the NCL 2014 Post Season Game: Web 1.  Where you needed to
# enter the captcha phrase (case sensitive) 10,000 times consecutively.  A wrong guess
# set the counter back to zero.  Due to it being a timed event, the code is very very
# sloppy.  I thought about cleaning it up and may do that some day but figured seeing
# bad code has its benefits.

# Usage.
# Ensure there is a captcha.png file and just execute the script.  It appropriately
# slice and cut the image.  Then open the Captcha + each letter and move the letters
# into the appropriate spot under iconset to strengthen the dictionary.


from PIL import Image
import hashlib
import time

im = Image.open("captcha.png")
im2 = Image.new("P",im.size,255)
im = im.convert("P")

temp = {}

print im.histogram()

for x in range(im.size[1]):
  for y in range(im.size[0]):
    pix = im.getpixel((y,x))
    temp[pix] = pix
    if pix == 0 or pix == 63: # these are the numbers to get
      im2.putpixel((y,x),0)

inletter = False
foundletter=False
start = 0
end = 0

letters = []

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

# New code is here. We just extract each image and save it to disk with
# what is hopefully a unique name

count = 0
for letter in letters:
  m = hashlib.md5()
  im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
  m.update("%s%s"%(time.time(),count))
  im3.save("./%s.gif"%(m.hexdigest()))
  count += 1
