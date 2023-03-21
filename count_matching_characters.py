#Count the Number of matching characters in a pair of string



def count_match_characters(s1,s2):
    count = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count += 1
    return count




s1 = input("Enter first string : ")
s2 = input("Enter second string: ")
count = count_match_characters(s1,s2)
print("Number of matching characters in a string : {}".format(count))

