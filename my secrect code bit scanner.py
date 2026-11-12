
secret_code = int(input("Enter your secret code: "))
access_key = int(input("Enter your access key: "))

# Convert numbers to binary
print("\nBinary representation:")
print("Secret code:", bin(secret_code))
print("Access key:", bin(access_key))

# 1. Scan bits
print("\nScanning secret code:")
for i in range(secret_code.bit_length()):
    bit = (secret_code >> i) & 1
    print("Bit", i, "=", bit)

# 2. Compare bits
print("\nComparing codes:")
if secret_code == access_key:
    print("Codes are equal")
else:
    print("Codes are different")

# 3. Flip bits
width = max(secret_code.bit_length(), 1)
mask = (1 << width) - 1
flipped = secret_code ^ mask

print("\nFlipped secret code:", bin(flipped))

# 4. Shift bits
print("\nLeft shift:", secret_code << 1)
print("Right shift:", secret_code >> 1)

# 5. Count bits
ones = secret_code.bit_count()
zeros = width - ones

print("\nNumber of 1 bits:", ones)
print("Number of 0 bits:", zeros)
