"""
range() function in Python (Before for loop)
--------------------------------------------
range() is a built-in function that generates
a sequence of numbers.

NOTE:
- range() does NOT display numbers automatically
- We must convert it into list, tuple, or access values manually
"""

# Creating a range object
numbers = range(5)
print(numbers)

# Output:
# range(0, 5)


print("\n--------------------\n")

# Converting range to list
numbers_list = list(range(5))
print(numbers_list)

# Output:
# [0, 1, 2, 3, 4]


print("\n--------------------\n")

# range(start, stop)
numbers_list = list(range(1, 6))
print(numbers_list)

# Output:
# [1, 2, 3, 4, 5]


print("\n--------------------\n")

# range(start, stop, step)
numbers_list = list(range(1, 10, 2))
print(numbers_list)

# Output:
# [1, 3, 5, 7, 9]


print("\n--------------------\n")

# Accessing values using index
r = range(10)
print(r[0])
print(r[3])
print(r[-1])

# Output:
# 0
# 3
# 9


print("\n--------------------\n")

#Length of range
r = range(1, 11)
print(len(r))

# Output:
# 10


print("\n--------------------\n")

# Using range() with while loop (allowed conceptually)
print("Using range() with while loop")

r = range(5)
i = 0

while i < len(r):
    print(r[i])
    i += 1
