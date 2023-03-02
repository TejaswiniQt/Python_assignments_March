'''
birthdays = { 'Harini'" : "April 13"" , """Srivani"" : "Oct 13"" , Ravi : Nov13, Tejaswini : Oct6 }

take input from user - Harini 
- check if the name is present in the birthdays
- if it is present - then print Harini's birthday is on April 13

- Leela 
- check 
- if not present update the dictionary birthdays 
[ ask user the birthday and update the dictionary ]
and print - the Birthday database is updated with Leela's birthday

You want to continue : yes or no 
Yes 
NO -- quit
'''

birthdays = {"Meghana":"Feb 26","Keerthana":"Dec 3","Nandini":"Aug 24"}
option = 'y'
while(option == 'y'):
    name = input("Enter the name: ")
    if name in birthdays:
            print("{} birthday is on {}".format(name,birthdays[name]))
    else:
        print("{} is not present in the list".format(name))
        birthdays[name] = input("Please provide the birthdate: ")
        print("Updated birthdays data: ",birthdays)
    option = input("Do you want to continue press 'Y' or 'N' : ")
