#Swap commas and dots in a String


def swap_commas_dots(s1):
    emp_str = ""
    for i in s1:
        if i == ',':
            emp_str = emp_str + '.'
        elif i == '.':
            emp_str = emp_str + ','
        else:
            emp_str = emp_str + i
    print("Ouput string: {}".format(emp_str))




s1 = input("Enter the string : ")
swap_commas_dots(s1)

