# ============================================
# List Comprehensions in Python
# ============================================

# What is a List Comprehension?
# A shorter and cleaner way to create a new list using a single line of code.

# Why do we need it?
# - Reduces code length
# - Improves readability (once understood)
# - Often faster than normal loops
# - Makes code look more Pythonic


# --------------------------------------------
# Basic Syntax
# --------------------------------------------

# [expression for item in iterable if condition]

# expression  -> What you want to store in the new list
# item        -> Variable representing each element
# iterable    -> Sequence (list, range, string, etc.)
# condition   -> Optional filter


# --------------------------------------------
# 1. Normal Loop vs List Comprehension
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Normal way
squares_loop = []
for n in numbers:
    squares_loop.append(n ** 2)

print("Squares using loop:", squares_loop)

# List comprehension way
squares_comp = [n ** 2 for n in numbers]

print("Squares using comprehension:", squares_comp)

# --------------------------------------------
# 2. Basic Transformation
# --------------------------------------------

numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

print("Squares:", squares)  # [1, 4, 9, 16, 25]


# --------------------------------------------
# 3. Filtering with Condition
# --------------------------------------------

evens = [n for n in range(1, 11) if n % 2 == 0]

print("Even Numbers:", evens)  # [2, 4, 6, 8, 10]


# --------------------------------------------
# 4. Transformation + Condition
# --------------------------------------------

even_squares = [n ** 2 for n in range(1, 11) if n % 2 == 0]

print("Even Squares:", even_squares)  # [4, 16, 36, 64, 100]


# --------------------------------------------
# 5. Nested Comprehension (Flattening a Matrix)
# --------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat_list = [num for row in matrix for num in row]

print("Flattened Matrix:", flat_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# --------------------------------------------
# 6. Conditional Expression (if-else inside)
# --------------------------------------------

labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]

print("Labels:", labels)
# ['odd', 'even', 'odd', 'even', 'odd']


# --------------------------------------------
# 7. Using Functions in Comprehensions
# --------------------------------------------

def square(n):
    return n * n

func_squares = [square(n) for n in range(1, 6)]

print("Function Squares:", func_squares)
# [1, 4, 9, 16, 25]


# --------------------------------------------
# 8. Multiple Conditions
# --------------------------------------------

# Numbers divisible by 4 (automatically divisible by 2 as well)
divisible_by_four = [n for n in range(1, 21) if n % 4 == 0]

print("Divisible by 4:", divisible_by_four)
# [4, 8, 12, 16, 20]


# --------------------------------------------
# Practice Tasks (Do It Yourself)
# --------------------------------------------

# 1. Create a list of cubes from 1 to 10 using list comprehension.
# 2. Create a list of numbers from 1–20 that are divisible by 3.
# 3. From a list of words, keep only words longer than 4 characters.
# 4. Flatten this matrix: [[10, 20], [30, 40], [50, 60]]
# 5. Create a list that labels numbers 1–10 as "small" if < 5 else "big".

