'''
2. check if the entered date is in  dd/sss/dddd i.e 06/JAN/2020
print statements accordingly
'''

def check_date(date):
    import re
    temp = re.compile(r'\d\d[/]*(JAN|FEB|MAR|APR|MAY|JUN|JLY|AUG|SEP|OCT|NOV|DEC)[/]*\d\d\d\d')
    res = temp.search(date)
    return res


date = input("enter the date: ")
res = check_date(date)
print(res)


