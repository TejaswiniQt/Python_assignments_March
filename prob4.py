'''
Create a new string made of the first, middle, and last characters of each input string
inp :
s1 = "America"
s2 = "Japan"
out: AJrpan
'''

str1 = input("Enter string1: ")
str2 = input("Enter string2: ")

len1 = len(str1) 
len2 = len(str2)
new_str = ""

new_str = new_str + str1[0] + str2[0]
new_str = new_str + str1[len1//2] + str2[len2//2] 
new_str = new_str + str1[len1-1] + str2[len2-1]


print("Output : %s"%new_str)

