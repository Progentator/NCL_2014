grep -i [a-z0-9] $1 |  sed 's/&.*\;//g' | sort | uniq
