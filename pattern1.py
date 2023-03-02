'''
Given an integer N, the task is to print half-diamond-star pattern.
Input: N = 3
Output:
*
**
***
**
*
'''


num = int(input("enter the number: "))
for i in range(num):
    for j in range(0, i+1):
        print("*", end = " ")
    print()

for i in range(1, num):
    for j in range(i, num):
        print("*", end = " ")
    print()
   
