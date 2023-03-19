#default arguments

#swap two numbers
#Example 1:

'''
#Example 1:

def swap_num(num1=10,num2): #syntax error : non default argument follows default argument
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))

#num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
swap_num(num2)
'''


#Example 2:
'''
def swap_num(num1,num2=20):
    print("Before argument: ")
    print("num1 = {}, num2 = {}".format(num1,num2))
    temp = num1
    num1 = num2
    num2 = temp
    print("After swapping: ")
    print("num1 = {}, num2 = {}".format(num1,num2))

num1 = int(input("Enter first number: "))
swap_num(num1)
'''

#Example 3:
'''
def fun(a,b,c,d=40):   #TypeError: fun() missing 1 required positional argument: 'c'
    print(a,b,c,d,end=" ")

fun(10,20)
'''

#Example 4:
'''
def fun(a,b,c,d=40):   
    print(a,b,c,d,end=" ")

fun(10,20,30,60)
'''

#Example 5:
'''
def fun(a,b,c=30,d=40):   
    print(a,b,c,d,end=" ")

fun(10,20)
'''

#Example 6:
'''
def fun(a,b=20,c,d=40):   #syntax error : non default argument follows default argument
    print(a,b,c,d,end=" ")

fun(10,20)
'''

#Example 7:
'''
def fun(a,b=20,c=30,d=40):   
    print(a,b,c,d,end=" ")

fun(10)
'''


#Example 8:

def fun(a,b=20,c=30,d=40):   
    print(a,b,c,d,end=" ")

fun(10,50)





