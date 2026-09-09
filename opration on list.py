classmates = ["Arav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class list:", classmates)

print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[:3])

classmates.append("meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sorted class list:", classmates)
classmates.reverse()
print("Reversed class list:", classmates)


teachers = {"name": "Mr. Sharma", "Subject": "Python", "Experience": 5}
print("\nTeacher profile:", teachers)

print("subject:", teachers["Subject"])
print("Experience:", teachers.get("Experience", "not found"))
teachers["Experience"] = 6
teachers["Email"] = "mr.sharma@school.com"
teachers.pop("Experience")
print("Updated teacher profile:", teachers)


roll_numbers = [1, 2, 3, 4, 5]
names = ["Arav", "Priya", "Rahul", "Sneha", "Meera"]
students_directory = dict(zip(roll_numbers, names))
print("student at roll number 3:", students_directory[3])