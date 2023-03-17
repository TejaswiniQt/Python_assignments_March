#Write a Python function to find the maximum of three numbers
#With arguments and with return type
'''
def maximum_of_three(num1,num2,num3):
    if num1>num2:
        max1 = num1
    else:
        max1 = num2
    if max1>num3:
        return max1
    else:
        return num3


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
max_num = maximum_of_three(num1,num2,num3)
print("The maximum of three number : {}".format(max_num))
'''

#with arguments and no return type
'''
def max_of_2(num1,num2):
    if num1>num2:
        print("maximum of nums: {}".format(num1))
    else:
        print("maximum of nums: {}".format(num2))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
max_of_2(num1,num2)
'''

#no arguments and no return type
'''
def fun():
    print("Hello")


fun()
'''

#no arguments and with return type

def sum_of_nums():
    a = 10
    b = 20
    print("Sum of numbers: {}".format(a+b))


res = sum_of_nums()
print(sum)

