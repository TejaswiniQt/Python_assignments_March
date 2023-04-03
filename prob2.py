'''
Create a string made of the middle three characters
Note :string length should be atleast 5
'''

str1 = input("Enter the string: ")
length = len(str1)
if length >= 5:
    mid = length // 2
    new_str = ""

    for i in range(len(str1)):
      if i == mid or i == mid-1 or i == mid+1:
         new_str = new_str + str1[i]

    print(new_str)
else:
    print("Length of the string shoulb be atleast 5")

