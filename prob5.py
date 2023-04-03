'''
Arrange string characters such that lowercase letters should come first
inp : str1 = PyNaTive
out: yaivePNT
'''

str1 = input("Enter string: ")
new_str = ""

for i in range(len(str1)):
    if str1[i].islower():
        new_str = new_str + str1[i]
for j in range(len(str1)):
    if str1[j].isupper():
        new_str = new_str + str1[j]

print("Output : %s"%new_str)

