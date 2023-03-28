'''
Python program to check prime number or not 
inp : 5
out : 5 is a prime number
'''

def prime_num(num):
    count = 1 
    for i in range(1,num//2+1):
        if num % i == 0:
            count += 1
    return count


num = int(input("Enter the number : "))
res = prime_num(num)
if res == 2:
    print("%d is a prime number"%num)
else:
    print("%d is not a prime number"%num)

