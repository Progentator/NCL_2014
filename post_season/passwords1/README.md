As always, send me a message if this isn't enough information for you and I'll be more than happy to explain it better.

Target: https://54.83.50.177/jHash.html

This was an interesting one.  There was a request to crack 21 passwords that used a custom hashing algorithm.  They supplied PHP Code to the hashing algorithm which was missing a really simple characterSplit function and 3 passwords that were used.  This was nice because it gave two things; a hint to what the theme of the password was (World of Warcraft) and way to verify the program worked after creating the missing function.

Since there was a lot of data loss in the hashing algorithm, reversing it was not an option and standard word lists showed a lot of collisions.  The best way to go about this one was to scrape WOWWiki but a problem became quickly apparent as the third password provided contained a space.  This meant that it wasn't as simple as stripping HTML and trying every single word.  Thankfully, every major character or town on the WOW Wiki has their own page.  This meant that it was possible to scrape the text which is inside the links and create semi decent wordlists.  

I created a script which would crawl WOW Wiki and scrape the links but am going to attach an older version because it doesn't do an infinite depth, and no logic of pages it has already been to.  Which means it createa A LOT of requests and won't stop until the script is terminated.  I will be attaching an earlier revision to where it is divided into two scripts, one to extract URL's and another to scrape the text of all the links in those URL's because of the above reason.

The workflow would be:

<ul>
	<li>python pages.py http://www.wowwiki.com/Undercity > urls</li>
	<li>python extract.py urls > words</li>
	<li>bash clean.py words > dict</li>
	<li>php bf.php dict</li>
</ul>

The root password was in an NCL Format, in order to generate that wordlist you could use `crunch 13 13 -t NCL-%%%%-,,,, -o FILE.OUT`
