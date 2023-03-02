#Guess the number

#To generate the random intteger number
import random
secret_num = random.randint(1,20)

for var in range(5):
    num = int(input("Enter the number: "))
    if num < secret_num:
        print("Your gues is less than the number")
    elif num > secret_num:
        print("Your guess is more than the number")
    else:
        print("your guess is correct")
        break
        
