'''
Append new string in the middle of a given string
inp :
s1 = "Ault"
s2 = "Kelly"
out: AuKellylt
'''

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

mid_len = len(str1)//2 
new_str = ""

for i in range(len(str1)):
    if i < mid_len:
        new_str = new_str + str1[i]
    else:
        if i == mid_len:
            new_str = new_str + str2 
        new_str = new_str + str1[i]

print("Output : %s"%new_str)

