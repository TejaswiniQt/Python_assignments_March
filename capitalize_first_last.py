#Python program to capitalize the first and last character of each word in a string
'''
Input: hello world 
Output: HellO WorlD
'''

inp = "hello world"
list1 = inp.split(sep=" ")
final_str = " "


for i in range(len(list1)):
    length = len(list1[i])
    str1 = list1[i]
    for j in range(len(list1[i])):
        if j == 0 or j == length-1:
            final_str = final_str + str1[j].upper()
        else:
            final_str = final_str + str1[j]
    final_str = final_str + " "


print(final_str)
            
