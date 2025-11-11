classA=[85, 90, 78, 92, 88, 76, 95, 89]

#add new addmission

classA.append(82)
print("after adding new admission:",classA)

#merging data of another class
classB=[80,91, 87]

classA.extend(classB)
print("after merging classB data:",classA)

#transfer student score removal
classA.remove(76)
print("after removing transfer student score:",classA)

#error conditon last entry remove
removed_score=classA.pop()
print("removed score was:",removed_score)
print("after removing last entry (error condition):",classA)

#performance review

print("heighest score in classA:", max(classA))
print("lowest score in classA:", min(classA))
print("total average:", sum(classA)/len(classA))
# print("total number of students in classA:", count(classA))
print("total number of students in classA:", len(classA))
print('location of score 90:', classA.index(90))
print('class a data in decending order:', sorted(classA, reverse=True))
