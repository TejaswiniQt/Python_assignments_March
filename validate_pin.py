#Validate PIN

#Reading the input pin from user x: pin = "1234"
pin = input("Enter the pin: ")

res = "False"
length = len(pin)
if (length == 4) or (length ==6):
    for k in pin:
        if ((ord(k) >= 48) and (ord(k) <= 57)):
            res = "True"
        else:
            res = "Flase"
            break
print(res)



