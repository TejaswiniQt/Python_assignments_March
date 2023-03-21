#reverse of a string

def str_reverse(s1):
    print("The reverse of a given string is : ",end=" ")
    for i in s1[-1::-1]:
        print(i,end="")


s1 = input("Enter the string: ")
res = str_reverse(s1)

