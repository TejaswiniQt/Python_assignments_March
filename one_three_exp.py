'''
{ Hema : 1 , Manoj : 1 , Vidya : 2 , Jyothsna : 3 , Ravi : 4 , Karthik : 6 , Yashaswini : 1.2 , Harini : 2.1 ,  Prashanth: 4.4 }
{ Hema : B&I , Manoj : QA , Vidya : QA , Jyothsna : QA , Ravi : DEV , Karthik : QA , Yashaswini : 1QA  , Harini : B&I ,  Prashanth: QA }
Write code using fns with parameters and return value : 
1.Print names of employees who are in range of 1-3 yrs of exp
'''

def one_three_exp(dic1):
    list1 = []
    for k,v in dic1.items():
        if v >= 1 or v <= 3:
            list1.append(k)
    return list1


db1 = {"Hema":1,"Manoj":1,"Vidya":2,"Jyothsna":3,"Ravi":4,"Karthik":6,"Yashaswini":1.2,"Harini":2.1,"Prashanth":4.4}
db2 = {"Hema":"B&I","Manoj":"QA","Vidya":"QA","Jyothsna":"QA","Ravi":"DEV","Karthik":"QA","Yashaswini":"QA","Harini":"B&I","Prashant":"QA"}

res = one_three_exp(db1)
print("The employees who are range of 1-3 experienced are : ",res,sep="\n")
