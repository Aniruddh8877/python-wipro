# a school want to calculate the average marks of a student and determine if the staudent qualifies for a merite certificate
#requeriments:
#1. marks in 3 subjects
#2 average = (subject1 + subject2 + subject3)/3
#3 boolean is_merit = average > 85



subject1 = float(input("Enter marks for subject 1: \n"))
subject2 = float(input("Enter marks for subject 2: \n"))
subject3 = float(input("Enter marks for subject 3: \n"))

average = (subject1 + subject2 + subject3) / 3
is_merit = average >= 85
# if is_merit:
#     return True
# else:
#     return False

print("Average marks :", average)
print("Qualified for Merit Certificate :", is_merit)