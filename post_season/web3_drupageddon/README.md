As always, send me a message if this isn't enough information for you and I'll be more than happy to explain it better.

Target: https://107.20.245.12

In October 2014, there was a very big SQL Injection in Drupal which allowed unauthenticated users full access to the database.  I recall reading on several placse that if you still were running Drupal <=7.31, you should consider your site compromised.  The full advisory is <a href="https://www.drupal.org/SA-CORE-2014-005">SA-CORE-2014-005 - Druapl core - SQL Injection</a>.  The funny/sad thing about this challenge is that it was constantly down because a destructive POC which changed the credentials of the first user (admin) had a higher page rank than the non-destructive Metasploit Module (exploit/multi/http/drupageddon).

That being said the metasploit module made its way into the main tree, the main catch is in order to use it you needed to enable SSL within the options.  The NCL Challenges enforced SSL where they could, most likely to avoid IDS Systems outside of their perimeter (College/WAN/etc).  Once you got admin credentials, you could view the revision history of the Flag Post and retrieve the flag.  Then use the database viewer to extract the hash of the Drupal user.  

It followed NCL Format, but cracking Drupal is very slow.  The NCL Passwords generally can be gotten without the need for Brute Forcing for hours, so it would be wise to do very specific NCL Formats such as "NCL-DRPL-####".  Generally, I tried a few dictionaries with basic rule sets (combine words, uCase first char of a word, add numbers to the end, etc) and when they failed I'd start the NCL Flag style.  My preferred method to crack Drupal is using cudaHashcat (oclHashcat for ATI users).
