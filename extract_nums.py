'''
1. extract all numbers from a string
'''


def extract_nums(string):
    import re
    temp = re.compile(r'\d')
    result = temp.findall(string)
    return result









string = "There are 8 people in the office, only 5 attended meeting"
res = extract_nums(string)
print(res)
