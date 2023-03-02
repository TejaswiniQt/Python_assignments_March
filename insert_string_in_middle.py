'''
Write a Python function to insert a string in the middle of a string.
input : "[[]] ""pyhton"
output: [[python]]
'''

def insert_str_middle(str1, str2):
    res = str1[:2] + str2 + str1[2:]
    return res



str1 = input("Enter the string ex:[[]] or <<>> etc : ")
str2 = input("enter the string to be inserted: ")
res = insert_str_middle(str1, str2)
print("Expected string : ",res)
