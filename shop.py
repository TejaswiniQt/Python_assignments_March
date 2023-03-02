
'''
List1 = [äpples ,"bananas", ""pineapples""]
Shopping list = [ apples, apples, bananas, apples, pear, pineapples, pear, apples,banana]
count the no.of times list1 elements are present in ShoppingList
ex: apples ==> 4 times in ShoppingList
'''

list_1 = ["apples","bananas","pineapples"]
shopping_list = ["apples", "apples", "bananas", "apples", "pear", "pineapples", "pear", "apples","bananas"]
count = 0
for i in range(len(list_1)):
    for j in range(len(shopping_list)):
        if list_1[i] == shopping_list[j]: #to serch for particular item in shoppping list
            count += 1
    print("count of {} in shopping list is: {} ".format(list_1[i],count))
    count = 0
        
