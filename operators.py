#Operators

num1 = int(input("enter the 1st number: "))
num2 = int(input("enter the 2nd number: "))
operator = input("Specify the math operation to be performed (+,-,*,/,%) : ")

if operator == '+':
    res = num1 + num2
    print("addtion of {} and {} is: {}".format(num1,num2,res))
elif operator == '-':
    res = num1 - num2
    print("subtraction of {} and {} is: {}".format(num1,num2,res))
elif operator == '*':
    res = num1 * num2
    print("Multiplication of {} and {} is: {}".format(num1,num2,res))
elif operator == '/':
    res = num1 / num2
    print("division of {} and {} is: {}".format(num1,num2,res))
elif operator == '%':
    res = num1 % num2
    print("Modulus of {} and {} is: {}".format(num1,num2,res))
