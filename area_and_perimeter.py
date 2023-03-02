# Program to find the area and perimeter of a rectangle

def area(l, b):
    area = l * b
    return area


def perimeter(l, b):
    p = (2*(l+b))
    return p


length=int(input("enter the length of rectangle: "))
breadth=int(input("enter the breadth of rectangle: "))
a = area(length,breadth)
p = perimeter(length,breadth)
print("Area of the rectangle is : ",a)
print("Perimeter of the traingle is : ",p)
