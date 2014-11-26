Recon 1 was simple nmap usage, I don't feel that I need to go into that one. 

Recon 2 was unique as it employed some type of weird technique I am not aware of.  Essentially, every closed port was open and would respond with random jibberish to make it hard for NMAP to detect what is open.  I'm sure there is probably a way to get NMAP to ignore those type of ports based upon retries not matching up.  However, I had done a simple ugly bash script to curl all ports looking for NCL in the response. `for i in `seq 1 65535`; do echo $i; curl -s http://54.204.15.112:$i |grep NCL; done`.

You can find 5 flags by simply examining the HTTP Source.  The final flag is in the /flag file.  There is no rhyme or reason how I found that other than a lucky guess.  
