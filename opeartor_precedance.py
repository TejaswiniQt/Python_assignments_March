#Operator precedance

a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp1 = a >> d * b % d + b
print(exp1)



a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp2 = f and d * c >> d
print(exp2)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp3 = a | c >> d + b * d
print(exp3)



a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp4 = b << d == a * f
print(exp4)



a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp5 = a // b + d & c - e
print(exp5)



a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp6 = f != b * d + c >> b ^ c
print(exp6)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp7 = b | c >= d + b ^ g * d ** c
print(exp7)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp8 = g + d or c // d
print(exp8)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp9 = a > d | e + c * f // b
print(exp9)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp10 = e * d - b + c * b or g // f
print(exp10)




a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp11 = a  % d | c >> b + g - b // d or a
print(exp11)



a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp12 = f - -d > g == c + a >> d & c ** b
print(exp12)

 

a,b,c,d,e,f,g = 6,2,10,1,5,8,9
exp13 = b + d is c >> d
print(exp13)


list1 = [10,2030,40,50]
print(20 not in list1)
print(50 in list1)

