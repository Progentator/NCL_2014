As always, send me a message if this isn't enough information for you and I'll be more than happy to explain it better.

Target: https://54.225.79.200

This was an odd target, all you were given is a login page which looked like it followed the Bootstrap theme.  DirBuster found that .htpasswd was accessible and it contained the hash of John Smith.  I'm not sure the "NCL Way" to get his password but I got it with a standard blind brute force.  It was a modified wordlist of just common words and the PasswordPro ruleset which does many things one of them is appending numbers to the end of each string.  The password was Badger1547.

Once you attempted to login you were greated with another prompt: 2FA, which obviously stood for 2 Factor Login.  Thankfully the webdeveloper left the webapp in some debug mode and posted "TOTP Code Block" and the users secret in the HTML Source Code.  The secret was: DN6KE7CM2L4NCQ64

TOTP, is a Time Based One Time Pad.  I've attached some source to generate the TOTP based upon this secret.  As always everything is hard coded just ensure you have the current time and execute the script.

