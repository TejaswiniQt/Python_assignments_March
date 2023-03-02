'''
L = [ name, gender, age, address]
D = [ name:sophie , gender:female , age : 6 , address: Hyderabad ]
if the item in the list is present in the dic -- print the item in the dict
else print : address is not present in D
print the val of that item/key
'''

l = ["name","gender","age","address"]
dic = {'name':'sophie','gender':'female','age':'6','address':'hyderabad'}
for i in range(len(l)):
    if l[i] in dic.keys():
        print('key:{}, value:{}'.format(l[i],dic[l[i]]))
    else:
        print("{} is not present in dictionary",l[i])
