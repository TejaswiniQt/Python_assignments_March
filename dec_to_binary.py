'''
Python program to check number representation is in binary

'''

def decimal_to_binary(num):
    temp = num
    list1 = []
    while num != 0:
        rem = num % 2
        num = num // 2
        list1.append(rem)
    print("%d in binary: "%(temp),end=" ")
    for i in list1[-1::-1]:
        print(i,end=" ")

num = int(input("Enter the number: "))
decimal_to_binary(num)

