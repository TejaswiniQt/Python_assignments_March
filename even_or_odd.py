'''
Python program to check given number is even or odd
inp : Enter the number: 5
out : 5 is an odd number
'''

def even_or_odd(num):
    if num % 2 == 0:
        print("%d is an even number"%num)
    else:
        print("%d is an odd number"%num)


num = int(input("Enter the number: "))
even_or_odd(num)

