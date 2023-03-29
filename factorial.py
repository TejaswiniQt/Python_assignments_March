'''
Python program to calculate the factorial using iterative approach
inp : Enter the number: 5
out : Factorial of 5 is: 120
'''

def factorial(num):
    prod = 1 
    for i in range(num):
        prod = prod * (i+1)
    return prod


num = int(input("Enter the number: "))
res = factorial(num)
print("Factorial of %d is: %d"%(num,res))

