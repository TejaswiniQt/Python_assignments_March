'''
Program to find the Sum of the digits of a given number
Input: n = 687
Output: 21

Input: n = 12
Output: 3
'''

def sum_of_digits(num,sum_num,rem):
    if num == 0:
        return sum_num
    rem = num % 10
    sum_num = sum_num + rem
    num = num // 10
    return sum_of_digits(num,sum_num,rem)


num = int(input("Enter the number: "))
sum_num,rem  = 0,0
res = sum_of_digits(num,sum_num,rem)
print("Sum of digits of %d is : %d"%(num,res))

