'''
Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
'''

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = []

for i in list1:
    length = len(i)
    if length > 0:
        list2.append(i)

print("Expected list: ",list2)
