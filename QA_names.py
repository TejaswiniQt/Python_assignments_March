'''
{ Hema : 1 , Manoj : 1 , Vidya : 2 , Jyothsna : 3 , Ravi : 4 , Karthik : 6 , Yashaswini : 1.2 , Harini : 2.1 ,  Prashanth: 4.4 }
{ Hema : B&I , Manoj : QA , Vidya : QA , Jyothsna : QA , Ravi : DEV , Karthik : QA , Yashaswini : 1QA  , Harini : B&I ,  Prashanth: QA }
Write code using fns with parameters and return value : 
4.Print QA names that  are in range of 2-3 yrs of exp
'''


def QA_names(dic1,dic2):
    for k,v in dic2.items():
        if v == 'QA':
            if k in dic1.keys():
                year = dic1[k]
                if year >= 2 and year <= 3:
                    print("{} is {} experienced in QA team".format(k,year))
            

db1 = {"Hema":1,"Manoj":1,"Vidya":2,"Jyothsna":3,"Ravi":4,"Karthik":6,"Yashaswini":1.2,"Harini":2.1,"Prashanth":4.4}
db2 = {"Hema":"B&I","Manoj":"QA","Vidya":"QA","Jyothsna":"QA","Ravi":"DEV","Karthik":"QA","Yashaswini":"QA","Harini":"B&I","Prashant":"QA"}



res3 = QA_names(db1,db2)
