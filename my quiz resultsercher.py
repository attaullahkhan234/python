
scores = [85, 90, 75, 95, 80, 90]

# Method 1: Direct Access
index = int(input("Enter index (0-5): "))

if 0 <= index < len(scores):
    print("Direct Access:", scores[index])
else:
    print("Invalid index")

# Method 2: Linear Search
target = int(input("Enter score to search: "))
found = False

for i in range(len(scores)):
    if scores[i] == target:
        print("Linear Search: Score found at index", i)
        found = True
        break

if not found:
    print("Score not found")

# Method 3: Pair Comparison
print("Pair Comparison:")

for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] == scores[j]:
            print("Matching scores:", scores[i],
                  "at indexes", i, "and", j)
