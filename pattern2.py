'''
Printing pyramid patterns in Python
i/P : num = 5
o/P :
* 
* * 
* * * 
* * * * 
* * * * *
'''

num = int(input("Enter the number: "))
for i in range(num):
    for j in range(0, i+1):
        print("*", end = " ")
    print()
