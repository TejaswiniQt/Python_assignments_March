'''
message = 'This is Python hands-on Programming and I want to make the most out of it .'
Count each character
add it to an empty dict
print the dict , at the end
'''

import pprint
message = "This is Python hands-on Programming and I want to make the most out of it"
new_dic = {}
for character in message:
    new_dic.setdefault(character, 0)
    new_dic[character] = new_dic[character] + 1
pprint.pprint(new_dic)

