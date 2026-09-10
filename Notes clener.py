n = int(input("How many characters to preview? "))
file = open("class_notes.txt", "r")
print(file.read(n))
file.close()


file =open("class_notes.txt", "r")
lines = file.readlines()
print("Total lines in the file:", len(lines))
for i in range (len(lines)):
    print(i + 1, "->", lines[i].strip())
print()


word = input("skip lines starting with: ")
filwe = open("class_notes.txt", "r")
for line in file:
    if  line.startswith(word):
        print("skip =>", line.strip())
file.close()
print()


file = open("class_notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines written to odd-lines.txt successfully!")