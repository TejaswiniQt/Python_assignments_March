#String slicing , string indexing 



s1 = "WELCOME"
'''
print(s1[3:])
print(s1[-1:])
print(s1[-1::-1])




for i in s1[-1::-1]:
    print(i)





for i in s1[-2:-4:-1]:
    print(i)




for i in range(len(s1)):
    print(s1[i],end=" ")





for i in range(len(s1)):
    print("s1[%d]="%i,s1[i],end=", ")




for i in range(len(s1)):
    print("s1[%d]"%s1)     #TypeError: %d format: a real number is required, not str




for i in range(1,len(s1)):
    print(s1[i],end=" ")




for i in range(1,len(s1),2):
    print(s1[i],end=" ")





for i in range(1,len(s1)-1):
    print(s1[i],end=" ")





for i in range(2,len(s1),2):
    print(s1[i],end=" ")





for i in range(2,len(s1),-2):
    print(s1[i],end=" ")





for i in range(len(s1),2,-1):
    print(s1[i],end=" ")  #IndexError: string index out of range





for i in range(-1,-(len(s1)),-1):
    print(s1[i],end=" ")





for i in range(-1,-(len(s1)+1),-1):
    print(s1[i],end=" ")
'''


s2 = "HELLO"

'''
print(s2[5])    #IndexError: string index out of range


print(s2[-1:-6:-1])


print(s2[-1:-6:-2])


print(s2[-1:-10:-1])


print(s2[0:10:1])


print(s2[0:5:0])   #ValueError: slice step cannot be zero


print(s2[0:5:-1])


print(s2[5:10:1])


print(s2[4:14:3])

'''



a = 142356
s4 = "HI"

print("a=%d"%a)

print("a=%s"%a)     #a=14365

print("a=%f"%a)   #a=14365.000000

print("a=%0.3f"%a)

print("s4=%s"%s4)

'''
print("s4=%d"%s4)  #TypeError: %d format: a real number is required, not str
'''

print("s4=%f"%s4)   #TypeError: must be real number, not str



