'''
Python program to remove character from string
Input String: embedded
Input Character : e
Output: mbddd (After removing ‘e’)
'''
def remove_character(str1,char):
    s1 = " "
    for i in range(len(str1)):
        if str1[i] != char:
            s1 = s1 + str1[i]
    return s1



str1 = input("Enter string: ")
char = input("Enter charcter to be removed: ")
res = remove_character(str1,char)
print("output : %s"%res)

