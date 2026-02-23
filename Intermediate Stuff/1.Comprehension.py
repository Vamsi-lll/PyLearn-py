# -------------------------------
# List Comprehensions in Python
# -------------------------------

# Syntax:
# [expression for item in iterable if condition]
# - expression: what you want to put in the new list
# - item: variable representing each element in the iterable
# - iterable: the sequence you loop through (list, range, etc.)
# - condition (optional): filter to include only certain items

# 1. Basic Transformation
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]  # square each number
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# 2. Filtering with Condition
evens = [n for n in range(1, 11) if n % 2 == 0]  # keep only even numbers
print("Evens:", evens)  # Output: [2, 4, 6, 8, 10]

# 3. Transformation + Condition
even_squares = [n**2 for n in range(1, 11) if n % 2 == 0]  # square only evens
print("Even Squares:", even_squares)  # Output: [4, 16, 36, 64, 100]

# 4. Nested Comprehension (Flattening a 2D List)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]  # flatten matrix
print("Flattened Matrix:", flat)  # Output: [1,2,3,4,5,6,7,8,9]

# 5. String Transformation
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]  # convert to uppercase
print("Uppercase Words:", upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# 6. Conditional Expression Inside Comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
print("Labels:", labels)  # Output: ['odd', 'even', 'odd', 'even', 'odd']

# 7. Using Functions in Comprehensions
def square(n):
    return n * n

func_squares = [square(n) for n in range(1, 6)]
print("Function Squares:", func_squares)  # Output: [1, 4, 9, 16, 25]

# 8. Nested Condition Example
mixed = [n for n in range(1, 21) if n % 2 == 0 if n % 4 == 0]
# keep numbers divisible by 2 AND 4
print("Divisible by 2 and 4:", mixed)  # Output: [4, 8, 12, 16, 20]

# 9. Dictionary Comprehension (bonus)
# Similar syntax but with key:value pairs
squares_dict = {n: n**2 for n in range(1, 6)}
print("Squares Dict:", squares_dict)  # Output: {1:1, 2:4, 3:9, 4:16, 5:25}

# 10. Set Comprehension (bonus)
unique_squares = {n**2 for n in [1, 2, 2, 3, 3, 4]}
print("Unique Squares Set:", unique_squares)  # Output: {16, 1, 4, 9}
