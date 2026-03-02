# ============================================
# Modules and Packages
# ============================================


# ============================================
# What is a Module?
# ============================================

# Modules and packages concepts play a key role in industry-grade projects.

# As we write more code, the file size and complexity of the project increase.
# Initially, it is easy to handle small-scale projects in a single file.

# But when the project grows, writing everything in a single file:
# - Makes the code messy
# - Makes debugging difficult
# - Makes maintenance hard
# - Reduces scalability

# To overcome this problem, we use MODULES.

# A module helps us:
# - Organize code properly
# - Improve readability
# - Improve maintainability
# - Improve scalability


# ============================================
# What Makes a Module?
# ============================================

# Every Python file (.py) is automatically a module.
# You don’t need to do anything special.

# Example:
# If you create a file named:

# math_operations.py

# That file itself is a module.


# ============================================
# What Makes Modules So Special and Powerful?
# ============================================

# The main power of modules is REUSABILITY.

# We already learned about the DRY principle:
# DRY = Don't Repeat Yourself

# When working with functions, we created a function once
# and reused it multiple times in the same file.

# But now with modules:
# We can reuse the same function in multiple different files.

# That is real power.


# ============================================
# Example of Creating a Module
# ============================================

# Create a file: math_operations.py

# Inside math_operations.py:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# ============================================
# Importing a Module
# ============================================

# Now create another file: main.py

# Basic Import
# import math_operations

# result = math_operations.add(5, 3)
# print(result)


# ============================================
# Import Specific Function
# ============================================

# from math_operations import add

# print(add(10, 5))


# ============================================
# Import With Alias
# ============================================

# import math_operations as mo
# print(mo.subtract(10, 3))


# ============================================
# Built-in Modules
# ============================================

# Python already provides many built-in modules.

# Example:

import math
print(math.sqrt(16))   # Output: 4.0

import random
print(random.randint(1, 10))


# ============================================
# What is a Package?
# ============================================

# A package is simply a folder that contains multiple modules.

# Example folder structure:

"""
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
"""

# The __init__.py file tells Python:
# "This folder should be treated as a package."


# ============================================
# Importing From a Package
# ============================================

# from my_package import module1

# or

# from my_package.module1 import some_function


# ============================================
# Why Packages Are Important?
# ============================================

# In large projects:
# - We cannot keep everything in one file.
# - We cannot even keep everything in one module.

# So we group related modules inside a package.

# Example:
# All database-related modules inside a database package.
# All API-related modules inside an api package.
# All authentication-related modules inside an auth package.


# ============================================
# Real-World Example
# ============================================

# Libraries like:
# - numpy
# - pandas
# - django

# are actually packages containing many modules.


# ============================================
# Practice Questions
# ============================================

# 1. Create a module named calculator.py with:
#    - multiply function
#    - divide function

# 2. Import only the multiply function into another file.

# 3. Import the whole module using an alias.

# 4. Create a package named utilities and place two modules inside it.
