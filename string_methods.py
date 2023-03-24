#String methods

#1.capitalize()
'''
str1 = "hello"
print(str1.capitalize())

str2 = "HELLO"
print(str2.capitalize())
'''

#2.casefold():  convert all characters to lowercase
'''
str1 = "MARIo"
print(str1.casefold())

str2 = "mario"
print(str2.casefold())

str3 = "maRio"
print(str3.casefold())
'''

#3.center() : The center() method will center align the string, using a specified character (space is default) as the fill character.
'''
str1 = "banana"
print(str1.center(20))
print(str1.center(20,"."))
print(str1.center(20,'*'))
'''


#4.count()
'''
str1 = 'abc_abc_abc_abc'
print(str1.count('ab'))
'''

#5. encode() The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
'''
str1 = "My name is Stale"
print(str1.encode())
print(str1.encode(encoding="ascii",errors="backslashreplace"))

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
'''

#6.endswith()
'''
str1 = "Tejaswini"
print(str1.endswith('i'))
'''


#7.starswith()
'''
str1 = "Tejaswini"
print(str1.startswith('T'))
'''

#8.expandtabs()
'''
str1 = "text1\text2\text3"
print(str1.expandtabs(20))


str2 = "text1/text2/text3"
print(str2.expandtabs(20))
'''


#9.find()
'''
str1 = "Hello world, Hi"
print(str1.find('Hi'))

str2 = "Hello world, Hi"
print(str2.find('is'))
'''

#10.format()
'''
str1 = "{} is learning {}"
print(str1.format('Tejaswini','Python'))
'''

#11.format_map()
'''
dic1 = {'x':10, 'y':-5}
str1 = 'dic1:({x},{y})'
print(str1.format_map(dic1))
'''

#12.index()
'''
str1 = "Hi world, Hello"
print(str1.index('Hi'))


str2 = "Hi world, Hello"
print(str2.index('is'))  #ValueError: substring not found
'''

#13.isalnum()
'''
str1 = "hello123"
print(str1.isalnum())


str2 = "hello*"
print(str2.isalnum())

str3 = "hello"
print(str3.isalnum())
'''

#14.isalpha()
'''
str1 = "hello123"
print(str1.isalpha())


str2 = "hello*"
print(str2.isalpha())

str3 = "Hello"
print(str3.isalpha())
'''

#15.isacii()
'''
str1 = "Hello"
print(str1.isascii())

str2 = "123,"
print(str2.isascii())
'''

#16.isdecimal()
'''
str1 = "123"
print(str1.isdecimal())

str2 ="340.235"
print(str2.isdecimal())
'''


#17.isdigit()
'''
str1 = "123"
print(str1.isdigit())

str2 ="340.235"
print(str2.isdigit())
'''

#18.isidentifier()
'''
str1 = "var_sum"
print(str1.isidentifier())

str2 = "1sum"
print(str2.isidentifier())

str3 = "_sum"
print(str3.isidentifier())
'''


#19.islower()
'''
str1 = "tejaswini"
print(str1.islower())

str2 = "Tejaswini"
print(str2.islower())
'''

#20.isupper()
'''
str1 = "Tejaswini"
print(str1.isupper())
'''

#21.isspace()
'''
str1 = "   "
print(str1.isspace())

str2 = "Hello hi"
print(str2.isspace())
'''

#22.istitle()
'''
str1 = "Tejaswini"
print(str1.istitle())

str2 = "tejaswini"
print(str2.istitle())
'''

#23.isprintable()
'''
str1 = "Hi, Hello"
print(str1.isprintable())

str2 = "Hi!, Hello\n"
print(str2.isprintable())
'''

#24.join()
'''
str1 = "-"
list1 = ['text1', 'text2', 'text3']
print(str1.join(list1))
'''




