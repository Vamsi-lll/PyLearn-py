#====================================================
#              LAMBDA FUNCTION IN PYTHON
#====================================================

# What is a lambda function?
# A lambda function is a small anonymous function.
# Anonymous means a function without a name.

# Lambda functions are mainly used for
# short and simple operations.


#====================================================
#           NORMAL FUNCTION vs LAMBDA
#====================================================

# Normal function
def square(num):
    return num * num

print(square(5))


# Same logic using lambda function
square_lambda = lambda num: num * num
print(square_lambda(5))


#====================================================
#               BASIC SYNTAX
#====================================================

# lambda arguments : expression

# Important points:
# - lambda functions can have multiple arguments
# - lambda functions can have only ONE expression
# - lambda functions automatically return the result


#====================================================
#               SIMPLE EXAMPLES
#====================================================

# Add two numbers
add = lambda a, b: a + b
print(add(10, 20))


# Check even or odd
is_even = lambda num: num % 2 == 0
print(is_even(4))
print(is_even(7))


# Find maximum of two numbers
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))


#====================================================
#               WHEN TO USE LAMBDA
#====================================================

# Use lambda when:
# - logic is very simple
# - function is used only once

# Avoid lambda when:
# - logic is complex
# - multiple lines are needed
