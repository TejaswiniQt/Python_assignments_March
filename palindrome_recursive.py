'''
Palindrome program in Python using recursive method 
inp : Enter the number : 121
out : 121 is a plaindrome number 
'''

def palindrome(rem,sum_num,num):
    if num == 0:
        return sum_num 
    rem = num % 10
    sum_num = sum_num * 10 + rem
    num = num // 10
    return palindrome(rem,sum_num,num)


num = int(input("Enter the number : "))
temp,rem,sum_num = num,0,0
res = palindrome(rem,sum_num,num)
if temp == res:
    print("%d is a plaindrome number"%num)
else:
    print("%d is not a palindrome number"%num)

