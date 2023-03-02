#Write a Python script to merge two Python dictionaries.

dic1 = {'a':100, 'x':500}
dic2 = {'m':900, 'p':600}
dic3 = dic1.copy()
dic3.update(dic2)
print(dic3)
