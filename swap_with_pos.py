#Given a list in Python and provided the positions of the elements,
#write a program to swap the two elements in the list.
'''
Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]
'''


list1 = []
n = int(input("Enter the number of elements : "))
for i in range(n):
    num = int(input())
    list1.append(num)
pos1 = int(input("Enter the position1: "))
pos2 = int(input("Enter the position2: "))
print("Before swapping: ",list1)
list1[pos1-1],list1[pos2-1] = list1[pos2-1],list1[pos1-1]
print("After swapping: ",list1)
    
