'''
String methods
'''
'''
#1. capitalize()

str1 = "hello world"
print(str1.capitalize())


#2. casefold()

str1 = "HeLLO WORLD"
print(str1.casefold())

#3.center()

str1 = "Hello"
print(str1.center(20))
print(str1.center(20,'.'))


#4. count()

str1 = "abc,abc,abc,abc"
print(str1.count('ab'))


#5.encode()

str1 = "My name is tejaswini"
print(str1.encode())


#6. endswith()

str1 = "Hello"
print(str1.endswith('o'))

str2 = "Hello"
print(str1.endswith('p'))


#7. expandtabs()

str1 = "text1\text2\text3"
print(str1.expandtabs(10))


#8. find()

str1 = "Helloee"
print(str1.find('e'))

str2 = "Hello"
print(str2.find('m'))


#9. format()

str1 = "{} learning {}"
print(str1.format('iam','Python'))


#10. index()

str1 = "Hello"
print(str1.index('l'))

str2 = "Hello"
print(str2.index('n'))


#12. isalnum()

str1 = "Hello123"
print(str1.isalnum())

str2 = "Hi"
print(str2.isalnum())

str3 = "123"
print(str3.isalnum())


#13. isalpha()

str1 = "Hello"
print(str1.isalpha())

str2 = "Hello123"
print(str2.isalpha())

str3 = "123"
print(str3.isalpha())


#14. isacii()

str1 = "Hello@"
print(str1.isascii())

str2 = "hello\n"
print(str2.isascii())


#15. isdecimal()

str1 = "1235"
print(str1.isdecimal())

str2 = "12.5"
print(str2.isdecimal())


#16. isdigit()

str1 = "1457"
print(str1.isdigit())

str2 = "12.5"
print(str2.isdigit())


#17. isidentifier()

str1 = "test_sample"
print(str1.isidentifier())

str2 = "Test_sample"
print(str2.isidentifier())

str3 = "_test"
print(str3.isidentifier())

str4 = "Hello@"
print(str4.isidentifier())


#18. islower()

str1 = "hello"
print(str1.islower())

str2 = "Hello"
print(str2.islower())


#19. isprintable()

str1 = "Hello world!"
print(str1.isprintable())

str2 = "Hello world\n"
print(str2.isprintable())

str2 = "Hello world\t"
print(str1.isprintable())


#20 isspace()

str1 = " "
print(str1.isspace())

str2 = "Hello"
print(str2.isspace())

str3 = "Hello "
print(str3.isspace())


#21. istitle()

str1 = "Hello"
print(str1.istitle())

str2 = "hello Hi"
print(str2.istitle())

str3 = "Hello Hi"
print(str3.istitle())


#22. isupper()

str1 = "TEJASWINI"
print(str1.isupper())

str2 = "HELLo"
print(str2.isupper())


#23. join()

str1 = '-'
list1 = ['text1', 'text2', 'text3']
print(str1.join(list1))

tup = ('10','20','30')
print('+'.join(tup))


#24. ljust()

str1 = "text"
print(str1.ljust(20,'-'))


#25. lower()

str1 = "HELLO"
print(str1.lower())

str2 = "Hello"
print(str2.lower())


#26. lstrip()

str1 = "Some text Some"
print(str1.lstrip('Some'))

str2 = "text Some"
print(str2.lstrip('Some'))


#27. partition()

str1 = 'a+b=c'
print(str1.partition('='))

str2 = 'a+b=c'
print(str2.partition('+'))


#28. removeprefix()

str1 = "Tejaswini"
print(str1.removeprefix('Teja'))

str2 = "Tejaswini"
print(str1.removeprefix('swini'))

str3 = "Tejaswini"
print(str3.removeprefix('T'))


#29. replace()

str1 = "Tejaswini S P"
print(str1.replace('S P','Paramesh'))

str2 = "Hello"
print(str2.replace('l','a'))


#30. rfind()

str1 = "Some text Some"
print(str1.rfind('S'))

str2 = "Some text Some"
print(str1.rfind('a'))


#30. rindex()

str1 = "Some text Some"
print(str1.rindex('S'))

str2 = "Some text Some"
print(str1.rindex('a'))   #ValueError: substring not found


#31. rjust()

str1 = "text"
print(str1.rjust(20,'-'))


#32. rpartion()

str1 = "a+b+c=a-b-c=a-v"
print(str1.rpartition('='))

str2 = "a+b+c=a-b-c=a-v"
print(str2.rpartition('-'))


#33. split()

str1 = "This is some special stuff"
print(str1.split(" "))


#34 rsplit()

str1 = "www website.com.http"
print(str1.rsplit('.'))

str2 = "www website com.http"
print(str2.rsplit('.'))


#35. rstrip()

str1 = "Some text Some"
print(str1.rstrip('Some'))

str2 = "Some text"
print(str2.rstrip('Some'))


#36. splitlines()

str1 = "this is some special case\n or else\n"
print(str1.splitlines(keepends=True))

str2 = "this is some special case\n or else\n"
print(str2.splitlines())


#37. startswith()

str1 = "Hello"
print(str1.endswith('e'))

str2 = "Hello"
print(str2.endswith('o'))


#38. strip()

str1 = "Some text Some"
print(str1.strip('Some'))

str2 = "Some text Some"
print(str2.strip('S'))


#39. swapcase()

str1 = "This is Tejaswini"
print(str1.swapcase())

str2 = "tHIS IS python"
print(str2.swapcase())


#40. title()

str1 = "this is some special stuff"
print(str1.title())


#41. upper()

str1 = "Tejaswini"
print(str1.upper())
'''

#42. zfill()

str1 = "test"
print(str1.zfill(20))

