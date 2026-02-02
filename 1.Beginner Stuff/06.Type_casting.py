# ====================================================
# Type Casting in Python
# ====================================================

# What is Type Casting?
# Type casting is the process of converting
# one data type into another data type.

# Why do we need Type Casting?
# Sometimes data is not in the format we need.
# Type casting helps us manipulate and use data
# based on the program requirement.


# ====================================================
# type() function
# ====================================================

# type() is a built-in function in Python.
# It is used to check the data type of a value or variable.

num = 10
print(type(num))  # <class 'int'>


# ====================================================
# Basic Type Casting Functions
# ====================================================

# Each data type in Python has its own function
# to convert data from one type to another.


# -------- Converting to int --------
# int() is used to convert a value to integer

x = 5.8
y = int(x)
print(y)
print(type(y))


# -------- Converting to float --------
# float() is used to convert a value to float

a = 10
b = float(a)
print(b)
print(type(b))


# -------- Converting to string --------
# str() is used to convert a value to string

num_value = 100
text = str(num_value)
print(text)
print(type(text))


# -------- Converting to boolean --------
# bool() is used to convert a value to boolean

value1 = 0
value2 = 1

print(bool(value1))  # False
print(bool(value2))  # True


# ====================================================
# Type Casting with Collection Types
# ====================================================

# Converting to list
tup = (1, 2, 3)
lst = list(tup)
print(lst)
print(type(lst))


# Converting to tuple
st = {4, 5, 6}
tup2 = tuple(st)
print(tup2)
print(type(tup2))


# Converting to set
lst2 = [1, 2, 2, 3]
st2 = set(lst2)
print(st2)
print(type(st2))
