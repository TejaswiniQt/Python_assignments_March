'''
Fibonacci series program in python using iterative method 
inp : Enter the number : 5
out : Fibonacii series: 
0 1 1 2 3 
'''

def fibonacci(num):
    num1,num2 = 0,1 
    print("Fibonacii series: ")
    print(num1,num2,sep=" ",end=" ")
    for i in range(1,num-1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3,sep=" ",end=" ")


num = int(input("Enter the number : "))
fibonacci(num)

