
# ============================================
# Tuple Collection Type in Python
# ============================================

# --------------------------------------------
# What is a Tuple?
# --------------------------------------------
# A tuple is a collection data type in Python
# used to store multiple values in a single variable.
# Tuple is similar to a list, but it is IMMUTABLE
# (once created, it cannot be changed).

# Example:
my_tuple = ("pylearn", 1, 2.5, True)


# --------------------------------------------
# Why do we need a Tuple?
# --------------------------------------------
# We use tuple when the data should NOT be changed.
# Example: days of a week, months, fixed configuration values.

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


# --------------------------------------------
# How to create a Tuple
# --------------------------------------------
# Tuples are created using parentheses ()

empty_tuple = ()
numbers = (1, 2, 3, 4)
mixed_tuple = ("python", 3.10, False)

# Single value tuple (IMPORTANT)
single_value = (10,)   # comma is mandatory


# --------------------------------------------
# Basic Operations on Tuple
# --------------------------------------------

languages = ("python", "java", "c++")

# Accessing elements using index
print(languages[0])   # python
print(languages[2])   # c++

# Length of tuple
print(len(languages))  # 3

# Tuple can be looped (iterable)
# (Loops will be explained later)


# --------------------------------------------
# Immutability of Tuple
# --------------------------------------------
# Tuple is an IMMUTABLE data type
# Meaning: we cannot modify its values

nums = (10, 20, 30)

# nums[1] = 200   ❌ This will raise an error


# --------------------------------------------
# Common Built-in Tuple Methods
# --------------------------------------------
# Tuple has very few methods because it is immutable

values = (1, 2, 2, 3, 4)

print(values.count(2))  # Count occurrences
print(values.index(3))  # Get index of value


# --------------------------------------------
# Mini Examples
# --------------------------------------------

# Example 1: Coordinates
point = (10, 20)

# Example 2: RGB color values
color = (255, 0, 0)

# Example 3: Nested tuple
nested = ((1, 2), (3, 4))


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a tuple with 5 elements.
# 2. Try modifying a tuple value and observe the error.
# 3. Create a single-value tuple.
# 4. Find the length of a tuple.
# 5. Count how many times a value appears in a tuple.
# 6. What is the main difference between list and tuple?
