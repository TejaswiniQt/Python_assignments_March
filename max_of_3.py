'''
Python Program to Find the max of 3 numbers
inp : 
Enter first number : 10
Enter second number : 12
Enter third number : 115
out :
115 is the grestest number
'''

def greatest_of_3(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        print("%d is the greatest number"%n1)
    elif n2 > n1 and n2 > n3:
        print("%d is the greatest number"%n2)
    else:
        print("%d is the grestest number"%n3)


n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
greatest_of_3(n1,n2,n3)

