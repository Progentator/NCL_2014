Warning: I do not believe this will work on Windows due to how the dictionary was built (Windows paths are not case sensitive).

This challenge was entering the correct Captcha code 10,000 times in a row consecutively!  If you failed a single captcha it would reset the score to 0.  Thankfully the captcha has a few flaws which made it easy to break:
<ul>
  <li>It used a single color exclusively for the character.  That meant we could search the canvis for that color and output it to a new canvis and unobstruct the image</li>
  <li>Characters did not overlap.  This made it trivial to cut the image up into pieces that only contained a single character, making it easy for OCR.</li>
</ul>

<strong>cut.py</strong> <br />
Creates an image for each of the characters in captcha.png; it is used to build the dictionary for the main solver.py script.  I recommend looking at both the captcha.png and each image when copying the files to the directory because it some characters can easily be mistaken otherwise such as O and o.  It is much easier to determine the size of the character when it is next to others.  

<strong>solve.py</strong><br />
This is where all the actual work is done.  It will enter the captcha phrase until it detects 9,999 in the header.  After it went to 9,999 consecutive entries.  I moved the break outside of the if statement in order to kill the loop and had it output the entire HTTP Page because I did not know what the page would look like or what would happen if it went beyong 10,000 tries.

<strong>Sources</strong><br />
<ul>
  <li><a href="http://www.boyter.org/decoding-captchas/">Decoding Captchas | Boyter.org</a>: Majority of the actual code came from here.</li>
</ul>
