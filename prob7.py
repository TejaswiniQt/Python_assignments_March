'''
Create a mixed String using the following rules
inp : 
s1 = "Abc"
s2 = "Xyz"
out: AzbycX
'''

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
len1 = len(str1)
len2 = len(str2)
new_str = ""
str2 = str2[-1::-1]

if len1 > len2:
    length = len1
else:
    length = len2

for i in range(length):
    if i < len1:
        new_str = new_str + str1[i]
    if i < len2:
        new_str = new_str + str2[i]
    
print(new_str)

    
    

