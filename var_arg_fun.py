#Variable argument function

#Example 1:
'''
def fun(*var):
    print(var)

fun(10,20,30,40)
'''


#Example 2:
'''
def fun(*var):
    print(var)

fun(10)
'''


#Example 3:
'''
def fun(*var):
    print(var)

fun("String",20,45)
'''


#Example 4:

def fun(*var):
    print("Tuple = {}".format(var))

fun()

