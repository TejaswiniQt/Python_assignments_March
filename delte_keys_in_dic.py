#Delete a list of keys from a dictionary

sample_dic = {
    "name": "Mike",
    "age" : 25,
    "salary" : 5000,
    "city" : "New york"
    }

print("Before deleting: ",sample_dic)
keys = ["name", "salary"]

for i in keys:
    sample_dic.pop(i)
print("After dleting: ",sample_dic)
