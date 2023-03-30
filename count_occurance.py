'''
Python Program to count occurrence of characters in string
Input String: embedded
Input Character : e
Output: Number of occurances of 'e' is : 3
'''
def count_occurance(str1,char):
    count = 0
    for i in range(len(str1)):
        if char == str1[i]:
            count += 1 
    return count



str1 = input("Enter string: ")
char = input("Enter character: ")
res = count_occurance(str1,char)
print("Number of occurances of '%s' is : %s"%(char,res))

#using string method 
'''
str1 = input("Enter string: ")
char = input("Enter character: ")
print(str1.count(char))
'''

