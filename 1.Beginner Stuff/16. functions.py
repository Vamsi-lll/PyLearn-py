#====================================================
#                 FUNCTIONS IN PYTHON
#====================================================

# What is a function?
# A function is a block of reusable code.
# Instead of writing the same code again and again,
# we write it once inside a function and call it whenever needed.

# Functions help us to:
# - Reduce code repetition
# - Improve readability
# - Make code modular and clean
# - Debug and maintain code easily


#====================================================
#             BASIC SYNTAX OF A FUNCTION
#====================================================

# def function_name():
#     function body
#     return value (optional)

# Note:
# - 'def' is a keyword used to define a function
# - function_name should follow variable naming rules
# - return is optional but recommended


#====================================================
#            SIMPLE FUNCTION EXAMPLE
#====================================================

def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()
greet()


#====================================================
#          FUNCTION WITH PARAMETERS
#====================================================

# Parameters are values passed into the function

def greet_user(name):
    print("Hello", name)

greet_user("Vamsi")
greet_user("Pylearn")


#====================================================
#          FUNCTION WITH RETURN VALUE
#====================================================

# return sends a value back to the caller

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum is:", result)


#====================================================
#        FUNCTION WITHOUT RETURN (VOID FUNCTION)
#====================================================

def show_message():
    print("This function does not return anything")

show_message()


#====================================================
#        FUNCTION WITH MULTIPLE RETURNS
#====================================================

def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)
print(add, sub, mul)


#====================================================
#        DEFAULT PARAMETER FUNCTION
#====================================================

def greet_country(name, country="India"):
    print(name, "is from", country)

greet_country("Vamsi")
greet_country("Alex", "USA")


#====================================================
#        KEY POINTS TO REMEMBER
#====================================================

# 1. Function code runs only when it is called
# 2. return is optional but useful
# 3. A function can return multiple values
# 4. Functions improve code quality and reusability
