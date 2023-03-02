'''
{ Hema : 1 , Manoj : 1 , Vidya : 2 , Jyothsna : 3 , Ravi : 4 , Karthik : 6 , Yashaswini : 1.2 , Harini : 2.1 ,  Prashanth: 4.4 }
{ Hema : B&I , Manoj : QA , Vidya : QA , Jyothsna : QA , Ravi : DEV , Karthik : QA , Yashaswini : 1QA  , Harini : B&I ,  Prashanth: QA }
Write code using fns with parameters and return value : 
2.check if the above name is a dev/B&I/QA
'''

def check_team(dic2,name1):
    for k in dic2:
        if k == name1:
            val = dic2[k]
    return val

db1 = {"Hema":1,"Manoj":1,"Vidya":2,"Jyothsna":3,"Ravi":4,"Karthik":6,"Yashaswini":1.2,"Harini":2.1,"Prashanth":4.4}
db2 = {"Hema":"B&I","Manoj":"QA","Vidya":"QA","Jyothsna":"QA","Ravi":"DEV","Karthik":"QA","Yashaswini":"QA","Harini":"B&I","Prashant":"QA"}

name = input("Enter the name : ")
res1 = check_team(db2,name)
print("{} is {} team".format(name,res1))
