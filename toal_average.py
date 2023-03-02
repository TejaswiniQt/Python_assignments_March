# Program to find the total and average for the given marks in 6 subjects

chem=float(input("Enter chemistry marks: "))
bio=float(input("Enter biology marks: "))
phy=float(input("Enter physics marks: "))
maths=float(input("enter mathematics marks: "))
eng=float(input("Enter english marks: "))
comp=float(input("enter computer science marks: "))

total=float(chem+bio+phy+maths+eng+comp)
average=(total/6)
print(average)
