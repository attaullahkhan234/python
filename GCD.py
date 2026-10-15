numberLargest = int(input("Enter Largest number: "))
numberSmallest = int(input("Enter Smallest number: "))

while(numberSmallest):
    numberstore = numberSmallest 
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberstore

print("HCF is", numberLargest)