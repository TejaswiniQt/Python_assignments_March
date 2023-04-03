'''
Write a program to count occurrences of all characters within a string
inp : str1 = "Apple"
out: {'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''

str1 = input("Enter string: ")
list1 = []
j,count = 0,0
length = len(str1)

while j < length:
    for i in range(len(str1)):
        if str1[j] == str1[i] and str1[j] not in list1:
            count += 1
    if str1[j] not in list1:
     print("'%s' : %d"%(str1[j],count),end=" ")
    list1.append(str1[j])
    count = 0
    j += 1
    

