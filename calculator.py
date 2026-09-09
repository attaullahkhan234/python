def add(a, b):
    print(a + b)

def subtraction(a, b):
    print(a - b)

def multiplication(a, b):
    print(a * b)

def division(a, b):
    print(a / b)

fnum = int(input("First number: "))
operation = input("Choose (+, -, *, /): ")
snum = int(input("Second number: "))

if operation == "+":
    add(fnum, snum)
elif operation == "-":
    subtraction(fnum, snum)
elif operation == "*":
    multiplication(fnum, snum)
elif operation == "/":
    division(fnum, snum)
else:
    print("Invalid operation")