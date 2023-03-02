#to check the phone number is valid or not


def valid_phone_num_or_not(num):
    res = 0
    length = len(num)
    if num[0:3] == '+91' and num[3] == '-':
        if length == 14:
            for k in (num[4:14]):
                if k >= '6' and k <= '9':
                    if not k.isdecimal():
                        res = 0
                    else:
                        res = 1
            if res == 0:
                print("Invalid number")
            else:
                print("Valid phone number")
        else:
            print("Invalid number: Invalid phone number length")
    else:
        print("Invalid number: Wrong country code or '-' is missing")
            
        

phnum = input("Enter the phone mumber in +XX - 10 digits format: ")
res = valid_phone_num_or_not(phnum)
