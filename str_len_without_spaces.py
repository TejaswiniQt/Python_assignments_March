# Avoid Spaces in string length



def str_len_without_spaces(s1):
    count = 0
    for i in s1:
        if i != " ":
            count += 1
    return count




s1 = input("Enter the string: ")
length = str_len_without_spaces(s1)
print("The length of a given string without spaces is : {}".format(length))

