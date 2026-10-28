input("set a bit - OR turns it on. press enter")
print("  5 =", bin(5)[2:])
print("  5 | 2=", 5 | 2, " binary:", bin(5 | 2)[2:])

input("Zero a bit - AND turns it off. press enter")
print("  7 =", bin(7)[2:])
print("  7 & 5=", 7 & 5, " binary:", bin(7 & 5)[2:])

n = int(input("Enter a number (try 4 or 6): "))
guess = input("is it a power of 2? (yes or no): ")
input("Power of 2 -- only one bit is ON. press enter")
if n > 0 and (n & (n - 1)) == 0:
    print("  ", n, " binary:", bin(n)[2:], "is a power of 2. your guess:", guess)
else:
    print("  ", n, " binary:", bin(n)[2:], "is NOT a power of 2. your guess:", guess)