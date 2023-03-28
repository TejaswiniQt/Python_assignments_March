'''
Python program to check Armstrong number or not 
inp : 153
out : yes it is a armstrong number
1^3 = 1 
5^3 = 125
3^3 = 27
1+125+27 = 153
'''

def armstrong_num(num):
    sum_num = 0
    while(num != 0):
        rem = num % 10
        cube = rem * rem *rem
        sum_num = sum_num + cube
        num = num // 10
    return sum_num


num = int(input("Enter the number : "))
res = armstrong_num(num)
if res == num:
    print("%d is an armstrong number"%num)
else:
    print("%d is not an armstrong number"%num)

