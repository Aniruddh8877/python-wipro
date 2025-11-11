#product managemet system

'''
a small company stores the number of product sold each day in a typle.
sales = (15,20,15,30,20,20,25)

tasks:
find the total number of product sold in a week
identity the day(s) when the max sales done
count how many days had sales equal to 20
'''

sales= (15,20,15,30,20,20,25)

#toal
total_sales = sum(sales)
print('total sales',total_sales)

#maximun sales
max_sales = max(sales)
max_index = sales.index(max_sales)
print('max sales:', max_sales,"on day ",max_index+1)

#count of day with sales =20
day_20_sales=sales.count(20)
print("number of day with sales = 20:",day_20_sales)

#reverse
#sales.reverse()
#print('reverse the tuple:',sales)

'''
fucntion:-
len, max, min, sum, sorted

method:-
count(obh),index(index,obj)
'''
