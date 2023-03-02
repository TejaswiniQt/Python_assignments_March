'''Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"] -> i/p
list2 = ["y", "me", "s", "lly"] -> i/p
['My', 'name', 'is', 'Kelly']   -> o/p
'''


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range(len(list1)):
    list3.append(list1[i]+list2[i])

print("concatenated list: ",list3)
        
