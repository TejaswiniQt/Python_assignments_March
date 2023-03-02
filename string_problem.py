'''
1.print the largest string in the list of strings
2.Print the no.of strings wholse length is >=5
3.print the count of strings which have first and last character same
'''

colours = ["red","green","yellow","white","brown","tet"] #list given
count1 = 0 #initializing the count to zero
count2 = 0
largest = 0

for val in colours:
    length = len(val)
    if length >= 5:     #checking the length of each string is greater than or equal to 5
        count1 += 1
    if length > largest:  #for finding the largest string in the list
        largest = length
        largest_string = val
    if val[0] == val[length-1]: #comapring first and last cahracters of each string in the list
        count2 += 1                   

print("Number of strings whose length is greater than 5 is: ",count1)
print("largest string in the list: ",largest_string)
print("Count of strings which has first and last characters are same = ",count2)
