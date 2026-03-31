
# ============================================
# Object-Oriented Programming (OOP) - Introduction
# ============================================


# ============================================
# What is OOP?
# ============================================

# OOP stands for Object-Oriented Programming.

# It is a way of writing code where we model real-world entities
# using classes and objects.

# Instead of writing everything as functions,
# we organize code into objects.


# ============================================
# Why Do We Need OOP?
# ============================================

# Without OOP:
# - Code becomes large and messy
# - Difficult to manage large projects
# - Hard to reuse code properly

# With OOP:
# - Code is organized
# - Easy to maintain
# - Reusable
# - Scalable
# - Used in real-world applications


# ============================================
# Real-World Example
# ============================================

# Think about a "Car"

# A car has:
# - Properties (color, brand, speed)
# - Actions (start, stop, accelerate)

# In OOP:
# - Properties → Variables
# - Actions → Methods (functions inside class)


# ============================================
# What is a Class?
# ============================================

# A class is a blueprint (template) for creating objects.

class Student:
    name = "Default Name"


# ============================================
# What is an Object?
# ============================================

# An object is an instance of a class.

s1 = Student()

# Accessing property
print(s1.name)


# ============================================
# Multiple Objects
# ============================================

s2 = Student()
s3 = Student()

print(s2.name)
print(s3.name)


# ============================================
# Key Points
# ============================================

# 1. Class = Blueprint
# 2. Object = Real instance
# 3. One class can create multiple objects


# ============================================
# Problem with Current Approach
# ============================================

# Right now, all objects have same data:
# name = "Default Name"

# This is not useful in real-world scenarios.

# We need dynamic values → This is solved using constructors.


# ============================================
# Introduction to Constructor (__init__)
# ============================================

# A constructor is a special method that runs automatically
# when an object is created.

class Student:
    def __init__(self, name):
        self.name = name


# Creating objects with different data
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)
print(s2.name)


# ============================================
# Understanding 'self'
# ============================================

# 'self' refers to the current object.

# It is used to store data inside the object.

# Example:
# s1.name → "Alice"
# s2.name → "Bob"


# ============================================
# Adding Methods to Class
# ============================================

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")


s1 = Student("Alice")
s1.greet()


# ============================================
# Summary
# ============================================

# - Class → Blueprint
# - Object → Instance
# - __init__ → Constructor
# - self → Refers to current object
# - Methods → Functions inside class


# ============================================
# Practice Questions
# ============================================

# 1. Create a class "Car" with:
#    - brand
#    - color

# 2. Create 2 objects with different values.

# 3. Add a method "start()" that prints:
#    "Car is starting"

# 4. Create a class "Student" with:
#    - name
#    - age
#    Add a method to display both.

# 5. Try creating 3 different objects and print their data.
