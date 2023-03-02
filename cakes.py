'''
Sort the list of strings ['bread', 'biscuit', 'cupcake', 'pastry', 'pancake'] -- the strings that start with 'p'should come first
and strings that strt with 'b' should go last
'''

list_cakes = ["bread","biscuit","cupcake","pastry","pancake"]
list_p = []
list_b = []
list_l = []
for item in list_cakes:
    if item[0] == 'p':
        list_p.append(item)
    if item[0] == 'b':
        list_b.append(item)
    elif (item[0] != 'p') and (item[0] != 'b'):
        list_l.append(item)

list_final = list_p + list_l + list_b
print("Sorted List: ",list_final)

