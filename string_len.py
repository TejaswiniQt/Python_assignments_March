#Length of a string in pyhton

def string_len(s1):
    count = 0
    for i in s1:
        count += 1
    return count


s1 = input("Enter the string: ")
length = string_len(s1)
print("Length of a string is : {}".format(length))

