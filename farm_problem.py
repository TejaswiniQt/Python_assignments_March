#Farm problem

chicken_legs = 2
cow_legs = 4
pig_legs = 4
chicken = int(input("Enter the number of chickens: "))
cow = int(input("Enter the number of cows: "))
pig = int(input("Enter the number of pigs: "))
total_chicken_legs = chicken * chicken_legs
total_cow_legs = cow * cow_legs
total_pig_legs = pig * pig_legs
total_legs = total_chicken_legs + total_cow_legs + total_pig_legs
print("Total animal legs: ",total_legs)
