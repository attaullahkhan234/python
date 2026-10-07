n = 10

guess = input ("Double Loop en n = 10. check n x n pairs. How many?")

input("Formula: one calculation done. press enter to run ")
steps = 1
print("steps =", steps, " -> o(1) constant time -> steps never changes")

input("Loop: one step per item. press enter to run ")
steps = 0
for i in range(n):
    steps += 1
print("steps =", steps, " your guess:", guess, " -> o(n) linear time -> steps grows with n")

input("Double Loop: checks every pair. press enter to run ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print("steps =", steps, " your guess:", guess, " -> o(n^2) quadratic time" )

input("Two more notations: press enter")
input(" big omega o -> best case lower bound")
input(" big theta o -> exact bound (worst = best) ")