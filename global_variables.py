#Global variables

def fun1():
    global a
    a = 50
    print(a)
    a = 80



a = 20
print(a)
fun1()
print(a)
