'''
scenario: event attendee management 
a company is organizing a tech conference. They want to manage 
the list of registered attendees using a set, because each attendee
 should be unique (no duplicate)


the system should be abe to:

add new attendee who register.
remove attendee who cancel their registration.
check if an attendee is registered.
combne lists of attendees from multiple events.
find common attendees between two events.

'''

attendees_event1 = {"aniruddh","bob","charlie","diana"}
attendees_event2 = {"charlie","eve","frank","alice"}


#add new attendee
attendees_event1.add("george")
print("after adding new attendee:", attendees_event1)

#remove attendee
attendees_event1.remove("bob")
print("after removing attendee:", attendees_event1)

#check if an attendee is registered
print("is alice registered for event1?", "alice" in attendees_event1)

#combine lists of attendees from multiple events
all_attendees = attendees_event1.union(attendees_event2)
print("all attendees from both events:", all_attendees)

#find common attendees between two events
common_attendees = attendees_event1.intersection(attendees_event2)
print("common attendees between event1 and event2:", common_attendees)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {9, 10, 11, 12, 13}

#union of sets
union_set = set1.union(set2, set3)
print("union of sets:", union_set)
