# My School Subject Planner

student = ("Khan", "4 ESO", 15, "Student")

print("Student details:", student)

print("Name:", student[0])

print("Class:", student[1])

print("Age:", student[2])

print("Role:", student[-1])


all_details = [student]

print("\nStudent name:", all_details[0][0])

print("Student class:", all_details[0][1])

print("Student details (sliced):", student[1:3])


print("\nStudent details:")

for detail in student:
    print(" -", detail)


monday_subjects = {"Math", "English", "Science", "PE", "History"}

tuesday_subjects = {"Math", "Spanish", "Computer Science", "English", "Art"}

print("\nMonday subjects:", monday_subjects)

print("Tuesday subjects:", tuesday_subjects)

print("Total Monday subjects:", len(monday_subjects))


monday_subjects.add("Geography")

monday_subjects.discard("PE")

print("\nUpdated Monday subjects:", monday_subjects)


all_subjects = monday_subjects.union(tuesday_subjects)

common_subjects = monday_subjects.intersection(tuesday_subjects)

only_monday_subjects = monday_subjects.difference(tuesday_subjects)

unique_to_both = monday_subjects.symmetric_difference(tuesday_subjects)


print("\nAll subjects:", all_subjects)

print("Common subjects:", common_subjects)

print("Subjects only on Monday:", only_monday_subjects)

print("Subjects unique to both days:", unique_to_both)