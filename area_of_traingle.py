# Program to find area of traingle


#Calculate the area of traingle
def area_traingle(b, h):
    a = (0.5 * b * h)
    return a


# Take the inputs
base=int(input("Enter the base: "))
height=int(input("enter the height: "))
area = area_traingle(base,height)
print("Area of the traingle is : ",area)
