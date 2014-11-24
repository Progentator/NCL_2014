Message me if you want a more traditional write up.  Otherwise here are notes.

Target: https://107.22.162.98/

This challenge had a webpage with Username+Password input boxes, a postgres elephant, and link to PhpMyAdmin.  The odd thing was if you sent non UTF-8 characters such as %91 or %92, the page would display the error message:

 Fatal error: Uncaught exception 'MongoException' with message 'non-utf8 string: ’' in /var/www/index.php:18 Stack trace: #0 /var/www/index.php(18): MongoCursor->rewind() #1 {main} thrown in /var/www/index.php on line 18

Mongo is vastly different and than SQL (Procedural vs Declarative Languages).  Anyways, the exploit is mainly dependent on the PHP Developer accessing $_GET directly and not doing any sanitizing.  For example:

<li>
	<ul>BAD:"username" => $_GET['username']</ul>
	<ul>GOOD:"username" => get('username', GET_STRING, '/^[a-zA-Z0-9]+$/')</ul>
</li>

Why's that bad?  Because PHP $_GET['variable'] could be any type of variable.  In this exploit we modify it to be an object, which causes the MongoDB driver to glitch and turn the NoSQL Query into a "Not Equals($ne)".

<li>
	<ul>Normal: ?username=admin&passwod=secret</ul>
	<ul>Exploit: ?username[$ne]=1&password[$ne]=1</ul>
</li>

Note: You do not need to have the 1 in the exploit query, it could be anything other than the legitimate value because it essentially changes == to !=.

That got you flags 1-3, I never got the fourth flag.  SynSyn hinted at it being in another database after the season was over, if I get time to go searching i'll update.

<b>Source</b>
<a href="https://www.idontplaydarts.com/2010/07/mongodb-is-vulnerable-to-sql-injection-in-php-at-least/"> MongoDB Is Vulnerable to SQL Injection in PHP At Least | IDontPlayDarts.com</a>

