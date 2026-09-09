file = open("My bucket list.txt", "w")
file.write("1. visit the eiffel tower\n")
file.write("2. Learn to play the guitar\n")
file.write("3. code my own game\n")
file.close()
print("Bucket list saved to 'My bucket list.txt'")


file = open("My bucket list.txt", "r")
content = file.read()
print("\n=== My Bucket List ===")
print(content)
file.close()



file = open("My bucket list.txt", "r")
lines = file.readlines()
print(f"you have {len(lines)} items in your bucket list.")
file.close()



file = open("My bucket list.txt", "a")
file.write("4. travel to Japan\n")
file.write("5. run a 5k marathon\n")
file.close()
print("\n 2 more items added!")



file = open("My bucket list.txt", "r")
print("\n=== Updated Bucket List ===")
print (file.read())
file.close()