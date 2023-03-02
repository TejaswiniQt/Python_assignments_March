#find the nth even number

num = int(input("Enter the number: " ))
if num % 2 == 0:
    quotient = num // 2;
    pos = quotient+1
    print("{} is {}th even number".format(num,pos))
    
