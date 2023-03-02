#invert list

list1 = [1, 2, 3, 4, 5]
list2 = []
list3 = []
for i in list1:
    if i > 0:
        num1 = -abs(i)
        list2.append(num1)
    else:
        num2 = abs(i)
        list3.append(num2)
new_list = list2 + list3
print(new_list)

