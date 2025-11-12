'''
Description
A college wants to manage students and the courses they register for.
Each student has a name, ID, registered courses, and GPA stored in different data structures.

Sample Input
students = [
{"id": 1, "name": "Ravi", "courses": ["Math", "Science",
"English"], "gpa": (8.5, 9.0, 8.8)},
{"id": 2, "name": "Sneha", "courses": ["Math",
"History"], "gpa": (9.2, 9.0)},
{"id": 3, "name": "Karan", "courses": ["Science",
"Computer"], "gpa": (7.5, 8.0)}
]
Operations to Perform
1. Add a new student: ID 4, Name “Priya”, Courses ["Math", "Computer",
"Economics"], GPA (8.8, 9.1, 9.0) using append().
2. Add a new course “AI” to Ravi’s courses using insert().
3. Remove course “History” from Sneha using remove().
4. Find average GPA for each student using sum() and len().
5. Find all unique courses offered using set() and update().
6. Sort students alphabetically by name using sort().

Expected Output
Added new student: Priya
Updated courses for Ravi: ['Math', 'AI', 'Science',
'English']
Removed 'History' from Sneha
Average GPA:
Ravi: 8.77 | Sneha: 9.1 | Karan: 7.75 | Priya: 8.97
All unique courses: {'Computer', 'Math', 'Science',
'English', 'Economics', 'AI'}
Students sorted by name: ['Karan', 'Priya', 'Ravi', 'Sneha']
'''

students = [
    {"id": 1, "name": "Ravi", "courses": ["Math", "Science", "English"], "gpa": (8.5, 9.0, 8.8)},
    {"id": 2, "name": "aniruddh", "courses": ["Math", "History"], "gpa": (9.2, 9.0)},
    {"id": 3, "name": "Karan", "courses": ["Science", "Computer"], "gpa": (7.5, 8.0)}
]      
print("Initial student data:", students, "\n")   

# 1. Add a new student
new_student = {"id": 4, "name": "akash", "courses": ["Math", "Computer", "Economics"], "gpa": (8.8, 9.1, 9.0)}
students.append(new_student)
print("Added new student:", new_student["name"])

# 2. Add a new course "AI" to Ravi's courses        
for student in students:
    if student["name"] == "Ravi":
        student["courses"].insert(1, "AI")
        print("Updated courses for Ravi:", student["courses"])
        break  
    

# 3. Remove course "History" from Sneha
for student in students:
    if student["name"] == "Sneha":
        student["courses"].remove("History")
        print("Removed 'History' from Sneha")
        break

# 4. Find average GPA for each student
print("Average GPA:")
for student in students:
    average_gpa = sum(student["gpa"]) / len(student["gpa"])
    print(f"{student['name']}: {average_gpa:.2f}", end=" | ")
print()

# 5. Find all unique courses offered
all_courses = set()
for student in students:
    all_courses.update(student["courses"])
print("All unique courses:", all_courses)

# 6. Sort students alphabetically by name
students.sort(key=lambda x: x["name"])
print("Students sorted by name:", [student["name"] for student in students]) 