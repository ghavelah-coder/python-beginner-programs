a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter +, -, *, /: ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/" and b != 0:
    print(a / b)
else:
    print("Invalid operation")
