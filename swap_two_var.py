'''
Swap two variables without using the third variable in Python
Input: a = 10, b = 20
Output: a = 20, b = 10
'''

def swap_num(num1,num2):
    num1 = num1 ^ num2
    num2 = num1 ^ num2
    num1 = num1 ^ num2
    print("After swapping: ",sep=" ")
    print("a = %d, b = %d"%(num1,num2))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: ",sep=" ")
print("a = %d, b = %d"%(num1,num2))
swap_num(num1,num2)

