# ============================================
# List Collection Type in Python
# ============================================

# --------------------------------------------
# What is a List?
# --------------------------------------------
# A list is a collection data type in Python that
# is used to store multiple values in a single variable.
# A list can store different types of data together.

# Example:
my_list = ["pylearn", 1, 2.5, True]


# --------------------------------------------
# Why do we need a List?
# --------------------------------------------
# Imagine storing marks of 5 students.
# Without list → you need 5 variables.
# With list → one variable is enough.

marks = [70, 80, 65, 90, 85]


# --------------------------------------------
# How to create a List
# --------------------------------------------
# Lists are created using square brackets []

empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = ["python", 3.10, True]


# --------------------------------------------
# Basic Operations on List
# --------------------------------------------

# Accessing elements using index
# (index starts from 0)
languages = ["python", "java", "c++"]
print(languages[0])   # python
print(languages[1])   # java

# Length of list
print(len(languages))  # 3

# Adding elements
languages.append("javascript")
print(languages)

# Removing elements
languages.remove("java")
print(languages)


# --------------------------------------------
# Mutability of List
# --------------------------------------------
# List is a MUTABLE data type
# Meaning: we can change its values after creation

nums = [10, 20, 30]
nums[1] = 200
print(nums)   # [10, 200, 30]


# --------------------------------------------
# Common Built-in List Methods
# --------------------------------------------

data = [1, 2, 3]

data.append(4)        # add element at end
data.insert(1, 100)   # insert at index
data.pop()            # remove last element
data.clear()          # remove all elements

print(data)


# --------------------------------------------
# Mini Examples
# --------------------------------------------

# Example 1: Storing user names
users = ["admin", "guest", "manager"]

# Example 2: Storing prices
prices = [99.9, 199.5, 299.0]

# Example 3: Nested list
matrix = [
    [1, 2],
    [3, 4]
]


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a list of 5 integers.
# 2. Change the 3rd element of a list.
# 3. Add a new element to an existing list.
# 4. Remove an element from a list.
# 5. Find the length of a list.
# 6. Create a list that stores mixed data types.
# 7. What happens if you try to access an index
#    that does not exist?
