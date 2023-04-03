'''
Arrange string characters such that lowercase letters should come first
inp : "P@#yn26at^&i5ve"
out: 
Total counts of chars, digits, and symbols 
Chars = 8, Digits = 3, Symbol = 4
'''

str1 = input("Enter string: ")
digit_count = 0 
chars_count = 0 
symbol_count = 0

for i in range(len(str1)):
    if str1[i].isdigit():
        digit_count += 1 
    elif str1[i].isalpha():
        chars_count += 1 
    else:
        symbol_count += 1 
print("Total counts of chars, digits and symbols : ")
print("Chars = %d, Digits = %d, Symbols = %d"%(chars_count,digit_count,symbol_count))

