#====================================================
#        while loop – Practice Problems
#====================================================
# Rules:
# - Use ONLY while loop
# - No for loops
# - Focus on logic and conditions


#====================================================
# Problem 1: Print numbers from 1 to 10
#====================================================

num = 1

while num <= 10:
    print(num)
    num = num + 1


#====================================================
# Problem 2: Print even numbers from 1 to 20
#====================================================

num = 1

while num <= 20:
    if num % 2 == 0:
        print(num)
    num = num + 1


#====================================================
# Problem 3: Sum of first N natural numbers
#====================================================

n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum is:", sum)


#====================================================
# Problem 4: Reverse a number
#====================================================

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)


#====================================================
# Problem 5: Count number of digits
#====================================================

num = int(input("Enter a number: "))
count = 0

while num > 0:
    count = count + 1
    num = num // 10

print("Number of digits:", count)


#====================================================
# Problem 6: Password retry system
#====================================================
# User gets unlimited attempts until password is correct

correct_password = "python"
entered_password = ""

while entered_password != correct_password:
    entered_password = input("Enter password: ")

print("Login successful")


#====================================================
# Problem 7: Menu driven program
#====================================================
# Simple calculator using while loop

choice = 0

while choice != 4:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == 4:
        print("Exiting program")

    else:
        print("Invalid choice")


#====================================================
# Problem 8: Guess the number (single round)
#====================================================

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

print("Correct guess!")


#====================================================
# Problem 9: Print multiplication table
#====================================================

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i = i + 1


#====================================================
# Problem 10: Check palindrome number
#====================================================

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")
