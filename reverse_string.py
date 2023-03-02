'''
2. Reverse a entire string using python?
'''
def reverse_string(string):
    return string[-1::-1]
    



string = input("Enter the string: ")
res = reverse_string(string)
print("Reversed string: ",res)
