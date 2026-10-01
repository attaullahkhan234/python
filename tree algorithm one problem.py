n=4
guess = input("Total points: 1 + 2 + 3 + 4 = ")

input("formula: one calculation. prees enter to run ")
total = n *(n + 1) // 2
print(" total =", total, "steps = 1")
input("Loop: adds one student at a time. press enter to run ")
total = 0
for student in range(1, n + 1):
    total += student
print(" total =", total, "steps =", n)

input("Nested loop: adds one point at a time. press enter to run ")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student + 1):
        total += 1
        steps += 1
print(" total =", total, "steps =", steps, "your guess was", guess)