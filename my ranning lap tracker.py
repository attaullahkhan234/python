
laps = int(input("Enter number of laps: "))

# Method 1: Formula
formula_points = laps * (laps + 1) // 2
print("Formula points:", formula_points)

# Method 2: Single Loop
loop_points = 0

for i in range(1, laps + 1):
    loop_points += i

print("Loop points:", loop_points)

# Method 3: Nested Loop
nested_points = 0

for i in range(1, laps + 1):
    for j in range(i):
        nested_points += 1

print("Nested loop points:", nested_points)
