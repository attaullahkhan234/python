import os

with open("math_notes.txt", "w") as file:
    file.write("Algebra equations and formulas\n")
    file.write("Practice quadratic equations\n")
    file.write("Review linear equations\n")

with open("science_notes.txt", "w") as file:
    file.write("Study the solar system\n")
    file.write("Review photosynthesis\n")
    file.write("Learn about cells\n")

with open("math_notes.txt", "r") as file:
    math_notes = file.read()

with open("science_notes.txt", "r") as file:
    science_notes = file.read()

math_words = len(math_notes.split())
science_words = len(science_notes.split())

print("Math words:", math_words)
print("Science words:", science_words)

if os.path.exists("study_notes.txt"):
    os.remove("study_notes.txt")

with open("study_notes.txt", "w") as file:
    file.write("===== MATH NOTES =====\n")
    file.write(math_notes)
    file.write("\n\n")
    file.write("===== SCIENCE NOTES =====\n")
    file.write(science_notes)

print("Study notes merged successfully!")