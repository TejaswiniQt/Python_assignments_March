#Python program to count number of vowels in given string


def count_vowels(s1):
    count = 0
    for i in s1:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count





s1 = input("Enter the string : ")
count = count_vowels(s1)
print("Number of vowels in a string : {}".format(count))

