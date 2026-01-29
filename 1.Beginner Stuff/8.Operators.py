#====================================================
#                  Python Operators
#====================================================

# Operators are used to perform operations on values and variables.
# Every operator in Python RETURNS a value after performing the operation.


#====================================================
#              1. Arithmetic Operators
#====================================================
# Used to perform mathematical calculations
# Return type: int or float

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333... (always returns float)
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Exponentiation → 1000


#====================================================
#              2. Comparison Operators
#====================================================
# Used to compare two values
# Return type: Boolean (True / False)

x = 5
y = 10

print(x == y)   # Equal to → False
print(x != y)   # Not equal to → True
print(x > y)    # Greater than → False
print(x < y)    # Less than → True
print(x >= y)   # Greater than or equal to → False
print(x <= y)   # Less than or equal to → True


#====================================================
#              3. Assignment Operators
#====================================================
# Do you remember in the previous talks we see the some examples using the = symbol this is called a assignment operator
# Used to assign values to variables
# Return type: None (they update the variable)

num = 10
num += 5   # num = num + 5 → 15
num -= 2   # num = num - 2 → 13
num *= 2   # num = num * 2 → 26
num /= 2   # num = num / 2 → 13.0

print(num)


#====================================================
#              4. Logical Operators
#====================================================
# Used to combine conditional statements
# Return type: Boolean (True / False)

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


#====================================================
#              5. Membership Operators
#====================================================
# Used to check if a value exists in a sequence
# Return type: Boolean (True / False)

list_data = [1, 2, 3, 4]

print(2 in list_data)      # True
print(5 not in list_data)  # True


#====================================================
#              6. Identity Operators
#====================================================
# Used to compare memory locations (same object or not)
# Return type: Boolean (True / False)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True


#====================================================
#              7. Bitwise Operators
#====================================================
# Used to perform bit-level operations
# Return type: int

x = 5   # 0101
y = 3   # 0011

print(x & y)   # AND → 1
print(x | y)   # OR → 7
print(x ^ y)   # XOR → 6
print(~x)      # NOT → -6
print(x << 1)  # Left Shift → 10
print(x >> 1)  # Right Shift → 2


#====================================================
#              8. Ternary Operator
#====================================================
# Also called Conditional Expression
# Used to write if-else in a single line
# Return type: Depends on condition result

age = 18

result = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(result)

# Syntax:
# value_if_true if condition else value_if_false
