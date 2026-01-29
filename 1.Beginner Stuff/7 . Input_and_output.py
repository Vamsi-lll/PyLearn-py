# ====================================================
# input() and output using print()
# ====================================================

# input() is a built-in function in Python.
# It is used to take input from the user.

# Just like print(), input() is available by default
# when Python is installed.

# Syntax:
# input("message")

# Whatever the user enters using input()
# is always returned as a string.


# ====================================================
# Basic input and output example
# ====================================================

name = input("Enter your name = ")
print("Hello", name)


# ====================================================
# Checking the data type of input
# ====================================================

# Even if the user enters a number,
# input() will still return a string.

age = input("Enter your age = ")
print(age)
print(type(age))


# ====================================================
# Using type casting with input
# ====================================================

# To work with numbers, we must type cast the input.

age_number = int(age)
print(age_number)
print(type(age_number))
