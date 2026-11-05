input("XOR swap - exchange values whitout third variable. press enter")
print(" before: a = 5, b = 10")
a, b = 5, 10
a ^= b; b ^= a; a ^= b
print(" after: a =", a, "b =", b)

n = int(input("Enter a number (try 3 or 7): "))
guess = input(" after XOR swap of "+ str(n) + " and 8 what does n become? ")
a, b = n, 8
a ^= b; b ^= a; a ^= b
input("XOR swap exchange the values. press enter")
print("  n becomes:", a, "  your guess:" , guess)
