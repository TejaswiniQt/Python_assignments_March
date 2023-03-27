#Program to Uppercase Half String
'''
Input : test_str = ‘tejaswini’ 
Output : tejaSWINI

Input : test_str = ‘apples’ 
Output : appLES 
'''

inp = "apples"
length = len(inp)//2
output = " "

for i in range(len(inp)):
    if i < length:
        output  = output + inp[i]
    else:
        output = output + str(inp[i]).upper()
        
print("Input : %s"%inp)
print("Output:%s"%output)

