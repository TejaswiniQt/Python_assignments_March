#keyword argument function

#Example 1:
'''
def fun(emp,age):
    print("emp = {}, age = {}".format(emp,age))

fun(emp="Harry",age=15)
'''


#Example 2:
'''
def fun(age,emp):
    print("emp = {}, age = {}".format(emp,age))

fun(emp="Harry",age=15)
'''


#Example 3:
'''
def fun(emp_name,age):  #TypeError: fun() got an unexpected keyword argument 'emp'
    print("emp = {}, age = {}".format(emp_name,age))

fun(emp="Harry",age=15)
'''


#Example 4:
'''
def fun(emp,age):   #TypeError: fun() got an unexpected keyword argument 'emp_name'
    print("emp = {}, age = {}".format(emp,age))

fun(emp_name="Harry",age=15)
'''

#Example 5:
'''
def fun(emp,age,branch="dev"):
    print("emp = {}, age = {}, branch = {}".format(emp,age,branch))

fun(emp="Harry",age=15)
'''


#Example 6:

def fun(age,emp,branch="dev"):
    print("emp = {}, age = {}, branch = {}".format(emp,age,branch))

fun(emp="Harry",age=15,branch="dev")




