'''
Python program for palindrome using an iterative method 
inp : Enter the number : 121
out : 121 is a plaindrome number 
'''

def palindrome(num):
    sum_num = 0
    while num != 0:
        rem = num % 10
        sum_num = sum_num * 10 + rem
        num = num // 10
    return sum_num


num = int(input("Enter the number : "))
temp = num
res = palindrome(num)
if temp == res:
    print("%d is a plaindrome number"%num)
else:
    print("%d is not a palindrome number"%num)

