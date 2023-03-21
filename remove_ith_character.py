#Ways to remove i’th character from string in Python


def remove_ith_chrac(s1,pos):
    emp_str = ""
    for i in range(len(s1)):
        if i != pos-1:
            emp_str = emp_str + s1[i]
    print("String after removing ith character: {}".format(emp_str))




s1 = input("Enter the string: ")
pos = int(input("Enter the position to remove the character from the string : "))
remove_ith_chrac(s1,pos)

