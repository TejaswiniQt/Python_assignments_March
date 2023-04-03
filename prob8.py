'''
Find all occurrences of a substring in a given string by ignoring the case
inp : "Welcome to USA. usa awesome, isn't it?"
out: The USA count is: 2
'''

str1 = input("Enter string: ")
str2 = input("Enter substring: ")

count = (str1.casefold()).count(str2.casefold())
print("The count of %s is: %d"%(str2,count))

