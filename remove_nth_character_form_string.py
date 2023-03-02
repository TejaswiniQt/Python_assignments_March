'''
Write a Python program to remove the nth index character from a nonempty string.
i/p : python
index = 3
o/P: pyton
'''

def remove_nth_index(str1, index):
    str1 = str1[:index] + str1[index+1:]
    return str1
    
    

string = input("Enter the string: ")
index = int(input("Enter the index to remove the character from the string: "))
res = remove_nth_index(string, index)
print("Expected result: ",res)

