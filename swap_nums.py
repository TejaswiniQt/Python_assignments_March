#Swap the numbers

#With arguments and With rerturn
'''
def swap_num(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: ")
print("num1 = {}, num2 = {}".format(num1,num2))
num1,num2 = swap_num(num1,num2)
print("After swapping: ")
print("num1 = {}, num2 = {}".format(num1,num2))
'''
#with arguments and without return
'''
def swap_num(num1,num2):
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swapping: ")
print("num1 = {}, num2 = {}".format(num1,num2))
swap_num(num1,num2)
'''

#without arguments and with return
'''
def swap_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Before swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))
    temp = num1
    num1 = num2
    num2 = temp
    return num1,num2

num1,num2 = swap_num()
print("After swapping: ")
print("num1 = {}, num2 = {}".format(num1,num2))
'''

#without arguments and without return

def swap_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Before swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))

swap_num()





