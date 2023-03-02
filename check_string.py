'''
1. extract all numbers from a string 
2. check if the entered date is in  dd/sss/dddd i.e 06/JAN/2020
print statements accordingly 
3.str ="" Twelve:12 Eighty nine:89 thirty-two:32""Print a all sub strings before :
 3.b split only on 1st occurance 
4. string = 'abc 12\
de 23 \n f45 6'
4.1Remove all whitespaces 
4.2: Remove all whitespaces and replace with $
5. ""Python is easy to learn ..but only if you practice Python it can be easy""
Check if ''Python'' is present in a given string or not 
6.str = ''12345 123 896 908 99765''
find : Three digit number followed by space followed by two digit number
'''

import re

'''
string = "There are 8 people in the office, only 5 attended meeting"

temp = re.compile(r'\d')
print(temp.findall(string))


date = input("enter the date: ")
temp = re.compile(r'\d\d[/]*(JAN|FEB|MAR|APR|MAY|JUN|JLY|AUG|SEP|OCT|NOV|DEC)[/]*\d\d\d\d')
print(temp.search(date))


string = "Twelve:12 Eighty nine:89 Thirty-two:32"
temp = re.compile(r"[A-Za-z\-\s]+")
print(temp.findall(string))

temp1 = re.compile(r"[A-Za-z\-\s]+")
print(temp1.search(string))


string = 'abc 12\
de 23 \n f45 6'

temp = re.compile(r'^(\s+)')
print(temp.findall(string))


string = "Python is easy to learn ..but only if you practice Python it can be easy"

temp = re.compile(r'Python')
mo = temp.search(string)
print(mo.group())
'''

str1 = '12345 123 89 908 99765'
temp = re.compile(r'\s\d\d\d\s\d\d')
mo = temp.search(str1)
print(mo.group())

