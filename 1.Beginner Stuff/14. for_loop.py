#====================================================
#                FOR LOOP IN PYTHON
#====================================================

# What is a for loop?
# A for loop is used to iterate (loop) over a sequence of elements.
# These elements can come from:
# - list
# - tuple
# - string
# - set
# - dictionary
# - range()

# The for loop executes a block of code once for each item in the sequence.


#====================================================
#                BASIC SYNTAX
#====================================================

# for variable in sequence:
#     code block

# Example:
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


#====================================================
#          FOR LOOP WITH range()
#====================================================

# range() is used when we know how many times the loop should run

# range(stop)
for i in range(5):
    print(i)        # output: 0 1 2 3 4


# range(start, stop)
for i in range(1, 6):
    print(i)        # output: 1 2 3 4 5


# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)        # output: 1 3 5 7 9


# Reverse looping
for i in range(10, 0, -1):
    print(i)


#====================================================
#        FOR LOOP WITH DIFFERENT DATA TYPES
#====================================================

# 1. List
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# 2. Tuple
tup = (1, 2, 3, 4)

for t in tup:
    print(t)


# 3. String
name = "PYTHON"

for ch in name:
    print(ch)


# 4. Set (unordered)
my_set = {10, 20, 30}

for item in my_set:
    print(item)


#====================================================
#        FOR LOOP WITH DICTIONARY
#====================================================

student = {
    "name": "alex",
    "age": 22,
    "course": "Python"
}

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, "=", value)


#====================================================
#           LOOP CONTROL STATEMENTS
#====================================================

# break -> stops the loop completely
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# continue -> skips current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# pass -> does nothing (placeholder)
for i in range(3):
    pass


#====================================================
#           ELSE WITH FOR LOOP
#====================================================

# The else block runs when the loop completes normally
for i in range(3):
    print(i)
else:
    print("Loop completed successfully")


#====================================================
#           NESTED FOR LOOP
#====================================================

# Loop inside another loop

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


#====================================================
#           REAL-LIFE EXAMPLE
#====================================================

# Printing multiplication table of a number

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
