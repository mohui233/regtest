
import re

line = "boooooooobby123"
regex_str = ".*(b.{1,}b).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print (match_obj.group(1))


