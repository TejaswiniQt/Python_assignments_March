#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

num = int(input("Enter the number: " ))
dic_sq = {}

for i in range(1, num+1):
    dic_sq[i] = i*i

print("Expected output : ",dic_sq)
