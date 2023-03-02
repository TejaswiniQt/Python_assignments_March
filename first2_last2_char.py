'''
Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
If the string length is less than 2, return the empty string instead
'''

def first2_last2_char(string):
    length = len(string)
    if length <= 2:
        return " "
    else:
        result = string[0:2] + string[length-2] + string[-1]
        return result



string = input("Enter the string: ")
res = first2_last2_char(string)
print("Expected string: ",res)
