'''
Scenario:
a company track emp and their current project 
'''

#emp dictinoary
emp={
     'e101':'website revamp',
     'e102':'mobile app',
     'e103':'data analysis',
}

#get the project of an  emp 
print("e102 is working on :",emp['e102'])
print('e102 is working on :',emp.get("e102"))

#add a new emp
emp['e141'] = 'cloud migration'

#remove an emp
emp.pop('e103')

#list all emp and their porject
for eid,project in emp.items():
    print(eid,'is working on',project)


#update project of an emp
emp.update({'e101':'website maintenance'})

print('after updating project:',emp)
