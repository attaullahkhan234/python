file = open("notes.txt", "r")

first_lines = file.read(3)
print(first_lines)

file.seek(0)

lines = file.readlines()

file.close()

clean_notes = []

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        clean_notes.append(line)

new_file = open("clean_notes.txt", "w")

for line in clean_notes:
    new_file.write(line)

new_file.close()

print("Clean notes saved to clean_notes.txt")