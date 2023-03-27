#Python program to print even length words in a string
'''
Input: s = "This is a python language"
Output: This is python language

Input: s = "i am tejaswini"
Output: am
'''

inp = "This is a python language"
list1 = inp.split(sep=" ")
output = " "

for i in list1:
    length = len(i)
    if length%2 == 0:
        output = output + i + " "
print("Input : %s"%inp)
print("Output:%s"%output)v

