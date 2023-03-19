#Required argument function


#Example 1:
'''
def fun(a,b,c):
    print(a,b,c,sep=" ")

fun(10,20,30)
'''


#Example 2:
'''
def fun(a,b,c): #TypeError: fun() missing 1 required positional argument: 'c'

    print(a,b,c,sep=" ")

fun(10,20)
'''

#Example 3:
'''
def fun(a,b):  #TypeError: fun() takes 2 positional arguments but 3 were given
    print(a,b,c,sep=" ")

fun(10,20,30)
'''

