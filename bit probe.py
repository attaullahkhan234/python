input("Bit diffrence - XOR shows which bits differ. press enter")
print("  5 ^ 3 =", 5 ^ 3, " binary:", bin(5 ^ 3), "  bit different:", bin(5 ^ 3).count("1"))
print("  12 ^ 5 =", 12 ^ 5, " binary:", bin(12 ^ 5), "  bit different:", bin(12 ^ 5).count("1"))

n = int(input("Enter a number (try 4 or 6): "))
guess = input("How many bits differ between " + str(n) + " and 7? ")
input("XOR marks the different bits. count the 1s. press enter")
diff = bin(n ^ 7).count("1")
print(" ", n, "^ 7 =", n ^ 7, " binary:", bin(n ^ 7), " bit different:", diff, " your guess:", guess)