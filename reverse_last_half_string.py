'''
Reverse last half of the string using  Python(using slicing)?
input : python
output : pytnoh
'''

def reverse_last_half_str(string):
    length =len(string)//2
    res = string[:length] + string[-1:length-1:-1]
    return res

string = input("Enter the string: ")
res = reverse_last_half_str(string)
print("Reversed string: ",res)
