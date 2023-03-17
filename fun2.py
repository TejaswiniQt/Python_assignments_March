#Default argument function

'''
def sum_of_nums(num1,num2=10):
    res = num1+num2
    print("sum of 2 numbers: {}".format(res))



num = int(input("Enter the number: "))
sum_of_nums(num)
'''


#Required argument function
'''
def req_arg_fun(a,b):    #TypeError: req_arg_fun() takes 2 positional arguments but 3 were given
    res = a+b
    print(res)


req_arg_fun(30,20,45)



def req_arg_fun(a,b,c):    
    res = a+b+c
    print(res)


req_arg_fun(30,20,45)
'''



#Variable argument function

'''
def var_arg_fun(*var):
    print(var)



var_arg_fun(5,8,3)
var_arg_fun("Python",50,45)
'''

#Keyword argument function

def max_of_2(num2,num1):
    if num1>num2:
        return num1
    else:
        return num2


maximum = max_of_2(num1=45,num2=20)
print("Maximum of 2 numbers: {}".format(maximum))

