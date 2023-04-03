'''
Create a string made of the first, middle and last character
'''

str1 = input("Enter the string: ")
length = len(str1)
mid = length // 2
new_str = ""

for i in range(len(str1)):
    if i == 0 or i == length-1 or i == mid:
        new_str = new_str + str1[i]

print(new_str)
    

