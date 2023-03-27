#Python program to check if a string has at least one letter and one number
'''
Input: welcome2ourcountry34
Output: True
Input: stringwithoutnum
Output: False
'''

inp = "welcome2ourcountry34"
letter = 0
num = 0

for i in range(len(inp)):
    if str(inp[i]).isalpha():
        letter = 1 
    if str(inp[i]).isdigit():
        num = 1 
    

if letter == 1 and num == 1:
    print("True")
else:
    print("False")

