#use regular expression to find the phone number in a big string

import re


phoneNumreg = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = phoneNumreg.search('Hello, this is my phone number. 9945346255 call me today.')
print(mo.group())
