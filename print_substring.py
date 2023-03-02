'''
3.a str ="" Twelve:12 Eighty nine:89 thirty-two:32""Print a all sub strings before :
3.b split only on 1st occurance
'''

def print_substring(msg):
    import re
    temp = re.compile(r"[A-Za-z\-\s]+")
    result = temp.findall(msg)
    return result

def only_first_occurance(msg1):
    import re
    temp = re.compile(r"[A-Za-z\-\s]+")
    result = temp.search(msg1)
    return result

string = "Twelve:12 Eighty nine:89 Thirty-two:32"
res = print_substring(string)
print("Sub strings are : ",res)

res1 = only_first_occurance(string)
print("Only first occurance in the string is : ",res1.group())


