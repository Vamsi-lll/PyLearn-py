# ============================================
# Collection Type - Data Types in Python
# ============================================

# As the name itself suggests, Collection Types
# are used to store a collection of data (multiple values).

# In Python, Collection Types are:
# - list
# - tuple
# - set
# - dictionary


# ============================================
# List Type
# ============================================

# List is a collection data type that can hold multiple values.
# It belongs to the class <class 'list'>
# Values are surrounded by square brackets []
# Values are separated by commas (,)
# List is a mutable data type (we can change it after declaration)
# List is an iterable (we can loop through it)

lst = ["pylearn", 1, 2.5]


# ============================================
# Tuple Type
# ============================================

# Tuple is a collection data type that can hold multiple values.
# It belongs to the class <class 'tuple'>
# Values are surrounded by parentheses ()
# Values are separated by commas (,)
# Tuple is an immutable data type (cannot be changed after declaration)
# Tuple is an iterable (we can loop through it)

tup = (1, 2, 3, 4, 5, 6)


# ============================================
# Set Type
# ============================================

# Set is a collection data type used to store multiple values.
# It belongs to the class <class 'set'>
# Values are surrounded by curly braces {}
# Values are separated by commas (,)
# Set does not allow duplicate values
# Set is an unordered collection (no fixed index)
# Set is mutable
# Set is an iterable

st = {1, 2, 3, 4, 5, 5}


# ============================================
# Dictionary Type
# ============================================

# Dictionary is a collection data type used to store data
# in the form of key-value pairs.
# It belongs to the class <class 'dict'>
# Values are surrounded by curly braces {}
# Each element is written as key : value
# Dictionary keys must be unique
# Dictionary is mutable
# Dictionary is an iterable

data = {
    "name": "pylearn",
    "version": 1,
    "rating": 4.5
}
