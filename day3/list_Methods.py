l1 = [10, 20, 30, 40, 50, 60]
print('the length of list :',len(l1))
print('the max value of the list',max(l1))
print('the min value of the list',min(l1))

l2 =[10,20,30,40]
# l2=['a','b','c']

def compare(l1,l2):
    if l1>l2:
        return 'l1 is greater'
    elif l1<l2:
        return 'l2 is greater'
    else:
        return 'both are equal' 

    return (l1>l2)-(l1<l2)

print(compare(l1,l2))



l3 = ('ANIRUDDH',23,'IT') #tuple

emp_list = list(l3) # tuple is converted to list(type casting)

print(l3)

#all the list methods is user in the file online shopping cart system
