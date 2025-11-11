'''
functions
s ={10,20,30,40,50}
s1=([10,20,30,40])


len(s)
min(s)
max(s)
sum(s)
set()


methods

s.add() add element to the set s
s.remove() remove element form set
s.discard() remove elemetn 30 when its found
s.pop() removes and returns an arbitrary element from the set
s.clear() removes all elements from the set
s.union() returns a new set with elements from both sets
s.intersection() returns a new set with elements common to both sets
s.difference() returns a new set with elements in the first set but not in the second set
s.symmetric_difference() returns a new set with elements in either the first or second set but not in both
s.update() updates the set by adding elements from another set or iterable

set is unordered and unique elements only
'''


s ={10,20,30,40,50}
# s.remove(300)
s.discard(300)
s.discard(30)
print(s)