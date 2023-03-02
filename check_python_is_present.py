'''
5. ""Python is easy to learn ..but only if you practice Python it can be easy""
Check if ''Python'' is present in a given string or not
'''

def check_python(msg):
    import re
    temp = re.compile(r'Python')
    result = temp.search(msg)
    return result


string = "Python is easy to learn ..but only if you practice Python it can be easy"
res = check_python(string)
print(res.group())


