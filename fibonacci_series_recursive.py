'''
Fibonacci series program in python using recursive method 
inp : Enter the number : 5
out : Fibonacii series: 
0 1 1 2 3 
'''

def fibonacci(n1,n2,num):
    if num == 0:
        return
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3,sep=" ",end=" ")
    num -= 1
    fibonacci(n1,n2,num)


num = int(input("Enter the number : "))
n1,n2 = 0,1 
print("Fibonacii series: ")
print(n1,n2,sep=" ",end=" ")
fibonacci(n1,n2,num-2)

