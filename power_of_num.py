'''
Given a number N and power P, the task is to find the power of a number ( i.e. NP ) using recursion.

Examples: 

Input: N = 2 , P = 3
Output: 8
'''

def power_of_num(num,power):
    if power == 0:
        return 1
    else:
        return num*power_of_num(num,power-1)




num = int(input("Enter the number: "))
power = int(input("Enter the power: "))
res = power_of_num(num,power)
print("{} power {} is: {}".format(num,power,res))
