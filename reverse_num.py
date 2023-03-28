'''
Python program to reverse a number 
inp : 123
out : 321
'''

def reverse_num(num):
    rev = 0
    while(num != 0):
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


num = int(input("Enter the number : "))
rev_num = reverse_num(num)
print("Reverse number : %d"%rev_num)

