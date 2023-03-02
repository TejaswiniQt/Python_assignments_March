'''
{ Hema : 1 , Manoj : 1 , Vidya : 2 , Jyothsna : 3 , Ravi : 4 , Karthik : 6 , Yashaswini : 1.2 , Harini : 2.1 ,  Prashanth: 4.4 }
{ Hema : B&I , Manoj : QA , Vidya : QA , Jyothsna : QA , Ravi : DEV , Karthik : QA , Yashaswini : 1QA  , Harini : B&I ,  Prashanth: QA }
Write code using fns with parameters and return value :  
3.Print all names & roles who have 1 yr exp
'''

def names_roles(dic1,dic2):
    for k,v in dic1.items():
        if v == 1:
            if k in dic2.keys():
                print("{} is in {} team who has one year experience".format(k,dic2[k]))

                

db1 = {"Hema":1,"Manoj":1,"Vidya":2,"Jyothsna":3,"Ravi":4,"Karthik":6,"Yashaswini":1.2,"Harini":2.1,"Prashanth":4.4}
db2 = {"Hema":"B&I","Manoj":"QA","Vidya":"QA","Jyothsna":"QA","Ravi":"DEV","Karthik":"QA","Yashaswini":"QA","Harini":"B&I","Prashant":"QA"}


res2 = names_roles(db1,db2)
