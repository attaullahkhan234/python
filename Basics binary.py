n = int(input("Enter a number (try 5 or 12): "))
guess = input("guess its binary : ")

input("binary. press enter ")
print(" decimal", n," binary", bin(n))
print("your guess", guess)

input("AND -- both bits must be 1. Press enter")
print("  12 =", bin(12)[2:],)
print("  10 =", bin(10)[2:],)
print("  12 & 10 =", 12 & 10)

input("OR -- either bit can be 1. Press enter")
print("  12 | 10 =", 12 | 10)