num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

print("\nChoose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = int(input("Enter your option: "))

if option == 1:
    print("Addition =", num1 + num2)
elif option == 2:
    print("Subtraction =", num1 - num2)
elif option == 3:
    print("Multiplication =", num1 * num2)
elif option == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print("Division =", num1 / num2)
else:
    print("Invalid option selected")
