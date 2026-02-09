# ============================================
# Set Collection Type in Python
# ============================================

# --------------------------------------------
# What is a Set?
# --------------------------------------------
# A set is a collection data type in Python
# used to store multiple values.
# A set does NOT allow duplicate values.
# A set is UNORDERED (no fixed position/index).

# Example:
my_set = {1, 2, 3, 4}


# --------------------------------------------
# Why do we need a Set?
# --------------------------------------------
# We use sets when:
# - We want only unique values
# - Order does not matter
# - We want fast membership checking

# Example: unique user IDs
user_ids = {101, 102, 103, 101}   # duplicate removed automatically
print(user_ids)


# --------------------------------------------
# How to create a Set
# --------------------------------------------
# Sets are created using curly braces {}

empty_set = set()        # IMPORTANT: {} creates dict, not set
numbers = {1, 2, 3, 4}
mixed_set = {1, "python", 2.5, True}


# --------------------------------------------
# Basic Operations on Set
# --------------------------------------------

# Adding elements
data = {1, 2, 3}
data.add(4)
print(data)

# Removing elements
data.remove(2)
print(data)

# Length of set
print(len(data))


# --------------------------------------------
# Unordered Nature of Set
# --------------------------------------------
# Set does NOT support indexing

values = {10, 20, 30}

# print(values[0]) This will raise an error


# --------------------------------------------
# Mutability of Set
# --------------------------------------------
# Set is MUTABLE
# Meaning: we can add or remove elements

items = {1, 2, 3}
items.add(5)
items.remove(1)
print(items)


# --------------------------------------------
# Common Built-in Set Methods
# --------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # combine sets
print(a.intersection(b)) # common elements
print(a.difference(b))   # elements in a not in b


# --------------------------------------------
# Mini Examples
# --------------------------------------------

# Example 1: Removing duplicates from a list
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print(unique_nums)

# Example 2: Allowed permissions
permissions = {"read", "write", "execute"}

# Example 3: Common subjects
student1 = {"math", "science", "english"}
student2 = {"science", "history", "english"}
print(student1.intersection(student2))


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a set with duplicate values and observe the output.
# 2. Add an element to a set.
# 3. Remove an element from a set.
# 4. Find common elements between two sets.
# 5. Remove duplicates from a list using a set.
# 6. Why does a set not support indexing?
