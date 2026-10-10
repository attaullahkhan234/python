
seats = [10, 20, 30, 40, 50, 60, 70, 80, 90]

input("List: " + str(seats) + " n=50 press enter to run ")
guess = input("Max checks to find a seat? ")
target = int(input("Enter a seat number to find: "))

input("Iterative binary search: press enter")
low, high = 0, len(seats) - 1
steps = 0

while low <= high:
    mid = (low + high) // 2
    steps += 1

    if seats[mid] == target:
        print("Found", target, "at index", mid,
              "in", steps, "steps. Your guess was", guess)
        break
    elif seats[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Seat not found in", steps, "steps.")

print("Iterative search: O(log n) time, O(1) space")

input("Recursive binary search: press enter")

def recursive_search(seats, low, high, target, steps=0):
    if low > high:
        print("Seat not found in", steps, "steps.")
        return

    mid = (low + high) // 2
    steps += 1

    if seats[mid] == target:
        print("Found", target, "at index", mid,
              "in", steps, "steps.")
    elif seats[mid] < target:
        recursive_search(seats, mid + 1, high, target, steps)
    else:
        recursive_search(seats, low, mid - 1, target, steps)

recursive_search(seats, 0, len(seats) - 1, target)

print("Recursive search: O(log n) time, O(log n) space")

input("Complexity ladder: press enter")

for n, s in [(9, 4), (100, 7), (1000, 10)]:
    print("n =", n, "steps =", s, "-> O(log n)")
