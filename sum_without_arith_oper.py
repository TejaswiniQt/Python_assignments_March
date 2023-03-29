'''
Python Program to add two numbers without addition operator
Input: a = 10, b = 20
Output: sum = 30
'''

def sum_of_num(num1,num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1 
    return num1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
res = sum_of_num(num1,num2)
print("Sum and %d and %d is: %d"%(num1,num2,res))

