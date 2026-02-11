def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = int(input("Enter your option: "))

match option:
    case 1:
        print("Addition =", add(num1, num2))
    case 2:
        print("Subtraction =", sub(num1, num2))
    case 3:
        print("Multiplication =", mul(num1, num2))
    case 4:
        print("Division =", div(num1, num2))
    case _:
        print("Invalid option selected")
