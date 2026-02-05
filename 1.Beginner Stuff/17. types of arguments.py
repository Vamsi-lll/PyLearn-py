#====================================================
#          TYPES OF ARGUMENTS IN PYTHON
#====================================================

# Arguments are the values passed to a function when it is called.
# Python supports multiple types of arguments to make functions flexible.


#====================================================
# 1. POSITIONAL ARGUMENTS
#====================================================

# These arguments are passed based on position (order).

def add(a, b):
    print(a + b)

add(10, 20)   # correct
# add(20, 10) -> order matters


#====================================================
# 2. KEYWORD ARGUMENTS
#====================================================

# Arguments are passed using parameter names.
# Order does not matter here.

def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=22, name="Vamsi")


#====================================================
# 3. DEFAULT ARGUMENTS
#====================================================

# Default values are used when no argument is provided.

def greet(name, country="India"):
    print(name, "is from", country)

greet("Vamsi")
greet("Alex", "USA")


#====================================================
# 4. VARIABLE-LENGTH ARGUMENTS (*args)
#====================================================

# *args allows passing multiple positional arguments.

def total_sum(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print(sum)

total_sum(10, 20)
total_sum(1, 2, 3, 4, 5)


#====================================================
# 5. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
#====================================================

# **kwargs allows passing multiple keyword arguments.

def user_details(**data):
    for key, value in data.items():
        print(key, ":", value)

user_details(name="Vamsi", course="Python", level="Beginner")


#====================================================
# 6. MIXED ARGUMENTS
#====================================================

# Order rule:
# positional → default → *args → **kwargs

def demo(a, b=10, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

demo(5, 20, 30, 40, name="Python", version=3.12)


#====================================================
#            KEY POINTS TO REMEMBER
#====================================================

# 1. Positional arguments depend on order
# 2. Keyword arguments improve readability
# 3. Default arguments avoid passing values every time
# 4. *args handles multiple values
# 5. **kwargs handles multiple key-value pairs
