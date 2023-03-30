'''
String Palindrome program in python
Input String: acca
Output: string is palindrome
'''
def palindrome(str1):
    rev_str = ""
    for i in str1[-1::-1]:
        rev_str = rev_str + str(i)
    if rev_str == str1:
        print("String is palindrome")
    else:
        print("String is not palindrome")


str1 = input("Enter string: ")
palindrome(str1)


