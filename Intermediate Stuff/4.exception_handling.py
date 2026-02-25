# ============================================
# Exception Handling in Python
# ============================================


# --------------------------------------------
# What is an Exception?
# --------------------------------------------
# An exception is an error that occurs
# during the execution of a program.
# If not handled properly, it stops the program.


# --------------------------------------------
# Why Do We Need Exception Handling?
# --------------------------------------------
# - Prevent program crash
# - Handle user input errors
# - Handle file errors
# - Make applications professional
# - Improve program stability


# --------------------------------------------
# Basic try-except Block
# --------------------------------------------

try:
    number = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# --------------------------------------------
# Handling Multiple Exceptions
# --------------------------------------------

try:
    num = int("abc")
except ValueError:
    print("Error: Invalid number")
except TypeError:
    print("Error: Type issue")


# --------------------------------------------
# Using 'except as e'
# --------------------------------------------

try:
    file = open("unknown.txt", "r")
except Exception as e:
    print("An error occurred:", e)


# --------------------------------------------
# Using else Block
# --------------------------------------------
# Runs only if NO exception occurs

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Division successful:", x)


# --------------------------------------------
# Using finally Block
# --------------------------------------------
# Always runs (even if error occurs)

try:
    value = 10 / 5
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("This block always runs")


# --------------------------------------------
# Real-World Example with File Handling
# --------------------------------------------

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as e:
    print("Unexpected error:", e)


# --------------------------------------------
# Raising Exceptions Manually
# --------------------------------------------

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


# --------------------------------------------
# Creating Custom Exception
# --------------------------------------------

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Access Granted")


try:
    check_age(15)
except InvalidAgeError as e:
    print("Custom Error:", e)


# --------------------------------------------
# Common Built-in Exceptions
# --------------------------------------------
# ZeroDivisionError
# ValueError
# TypeError
# FileNotFoundError
# IndexError
# KeyError


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Handle division by zero error.
# 2. Handle file not found error.
# 3. Create a custom exception for invalid password.
# 4. Use try-except-else-finally in one program.
# 5. Raise an error if a number is negative.
