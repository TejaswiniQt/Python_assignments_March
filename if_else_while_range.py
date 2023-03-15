#if statement
#check Entered number greater than 50

'''
def check_greater_num(num):
    if num>50:
        print("%d is greater than 50",num)


num = int(input("Enter the number: "))
check_greater_num(num)
'''

'''
#To check the entered number is even or odd
def even_odd(num):
    if num%2 == 0:
        return 1
    else:
        return 0

num = int(input("Enter the number: "))
res = even_odd(num)
if res == 1:
    print("{} is even number".format(num))
else:
    print("{} is odd humber".format(num))
'''


'''
#Program to accept percentage from the user and display the according to the following criteria
Marks         Grade
>90            A
>80 and <=90   B
>=60 and <=80  c
<60            D
'''
'''
def grade(marks):
    if marks>90:
        print("A Grade")
    elif marks>80 and marks<=90:
        print("B Grade")
    elif marks>=60 and marks<=80:
        print("C Grade")
    else:
        print("D Grade")

marks = int(input("Enter the marks: "))
grade(marks)
'''

'''
#Nested if else


num = int(input("Enter the number: "))

if num <= 100:
    if num >= 75:
        print("Greater than or equal 75")
    else:
        print("Less than 75")
else:
    if num >= 200:
        print("Greater than or equal to 200")
    else:
        print("Less than 200")
    
'''

'''
#Print first 10 intergers and their squares using while loop

num = 1
while(num <= 10):
    print("{} square is {}".format(num,num*num))
    num += 1
'''

#example for break, continue and pass
'''
num = 1

while(num <= 10):
    if num == 6:
        break
    else:
        print(num,end=" ")
    num += 1

num = 0

while(num <= 10):
    num += 1
    if num == 6:
        continue
        print(num)
    else:
        print(num,end=" ")

num = 1

while(num <= 10):
    if num == 6:
        pass
        print(num, end=" ")
    else:
        print(num,end=" ")
    num += 1
'''


#range()

for i in range(5):
    print(i,end=" ")
print(" ")

for i in range(1,10):
    print(i,end=" ")
print(" ")

for i in range(1,10,2):
    print(i,end=" ")
print(" ")

for i in range(10,1,-2):
    print(i,end=" ")


