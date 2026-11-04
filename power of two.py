input("power of 4: n % 3 == 1   power of 8: n % 7 == 1. press enter")
print(" 16 binary:", bin(16)[2:], " 16 % 3 =", 16 % 3, " power of 4: yes")
print(" 8 binary:", bin(8)[2:], " 8 % 7 =", 8 % 7, " power of 8: yes")

n = int(input("Enter a number (try 64 or 32): "))
guess = input("is " + str(n) + " a power of 4? (yes or no): ")
input("check: n % 3 == 1. press enter")
is_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
if is_pow4:
    print("  ", n, " binary:", bin(n)[2:], "is a power of 4. your guess:",
            guess)
else:
    print("  ", n, " binary:", bin(n)[2:], "is NOT a power of 4. your guess:",
            guess)