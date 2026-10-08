scores = [1, 3, 5, 7, 9, 11, 13, 15, 17,]

input("List: " +str(scores) + " n=9 press enter to run ")
guess = input("Max checks to find any number in the list? ")
target = int(input("Enter a number to find in the list: "))

input("binary search: checks the middle, drops half each round. press enter")
low, high = 0, len(scores) - 1
steps = 0
while low <= high:
    mid = (low + high) // 2
    steps += 1
    print("Found", target, "at index", mid, "in", steps, "steps. Your guess was", guess)
    if scores[mid] == target:
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print(" found", target, "at position", mid + 1, "in", steps, "steps your guess was", guess, "->  o(log n) ")

input("steps grow slowly with n. press enter to run ")
for n, s in [(9, 4), (100, 7), (1000, 10), ]:
    print("n =", n, "steps =", s, " -> o(log n)")