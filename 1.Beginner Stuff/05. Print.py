# =============================================
# Introduction to print() function
# =============================================

# print() is a powerful built-in function in Python.
# It comes by default when we install Python.
# We do not need to import anything to use it.

# What does print() do?
# print() is mainly used to display output on the screen.
# It helps us see:
# - values
# - variables
# - results of operations
# - messages for the user


# =============================================
# Basic example
# =============================================

name = "Pylearn"
print(name)

# Output:
# Pylearn


# =============================================
# Printing values directly
# =============================================

# We can directly pass a value inside print()
print("pylearn")

# Output:
# pylearn


# =============================================
# Printing text with variables
# =============================================

print("Project name is:", name)

# Output:
# Project name is: Pylearn


# =============================================
# Printing multiple values
# =============================================

version = 1
print("Name:", name, "Version:", version)

# Output:
# Name: Pylearn Version: 1


# =============================================
# print() function attributes (basic intro)
# =============================================

# print() has some useful attributes like:
# - end
# - sep
# We will learn them one by one.


# end attribute example
print("Hello", end=" ")
print("World")

# Output:
# Hello World


# sep attribute example
print("Python", "is", "awesome", sep=" - ")

# Output:
# Python - is - awesome
