import os

print("=== science notes ===")
with open("science_notes.txt", "r") as f:
   for line in f:
      print(line.strip())
print()


print("=== word count ===")
with open("math_notes.txt", "r") as f:
   for line in f:
    words = line.split()
   print(len(words), "words->", line.strip())
print()


print("=== merging notes ===")
if os.path.exists("all_notes.txt"):
   print("all_notes.txt already exists - overwriting...")
else:
    print("all_notes.txt does not exist - creating...")

content = ""
with open("science_notes.txt", "r") as f:
   content += "--- Science Notes ---\n"
   content += f.read() + "\n"
with open("math_notes.txt", "r") as f:
   content += "--- Math Notes ---\n"
   content += f.read() + "\n"
with open("all_notes.txt", "w") as out:
   out.write(content)
print("saved to all_notes.txt")
print()

if os.path.exists("all_notes.txt"):
   os.remove("all_notes.txt")
   print("all_notes.txt deleted")
else:
   print("all_notes.txt does not exist")