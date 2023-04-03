'''
Calculate the sum and average of the digits present in a string
inp : "PYnative29@#8496"
out: Sum is: 38 Average is  6.333333333333333
'''

str1 = input("Enter string: ")
sum_num = 0
count = 0

for i in range(len(str1)):
    if str1[i].isdigit():
        sum_num = sum_num + int(str1[i])
        count += 1

avg = sum_num/count
print("Sum is:", sum_num, "Average is ", avg)

