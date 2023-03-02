'''
6.str = ''12345 123 896 908 99765''
find : Three digit number followed by space followed by two digit number
'''

def check_3digit(msg):
    import re
    temp = re.compile(r'\s\d\d\d\s\d\d')
    result = temp.search(msg)
    return result

str1 = '12345 123 89 908 99765'
res = check_3digit(str1)
print("3 digit followed by 2 digit:",res.group())

