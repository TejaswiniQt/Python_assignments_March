#swap first and last elements in the list



list1 = [10,20,30,40,50]
length = len(list1)
if length >= 2:
    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp
print(list1)
