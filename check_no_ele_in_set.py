#Write a Python program to check if two given sets have no elements in common.

set1 = {1,2,3,4}
set2 = {5,6,7,8}
set3 = {3,9}

print("comparing set1 and set2: ",set1.isdisjoint(set2))
print("Comparing set1 and set3: ",set1.isdisjoint(set3))
print("Comparing set2 and set3: ",set2.isdisjoint(set3))
