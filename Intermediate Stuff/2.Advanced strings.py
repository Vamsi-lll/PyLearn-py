# ============================================
# String Data Type in Python - Part 2
# (Advanced String Methods & String Types)
# ============================================


# --------------------------------------------
# Types of Strings in Python
# --------------------------------------------

# Normal String
normal_string = "Hello Python"
print(normal_string)

# Raw String (r"")
# Used to ignore escape characters
raw_string = r"C:\Users\new_folder\test"
print(raw_string)

# Without raw string:
# "C:\Users\new_folder\test"  -> may cause escape issues

# f-String (Formatted String)
name = "Alex"
age = 25
f_string = f"My name is {name} and I am {age} years old"
print(f_string)

# Multi-line String
multi_line = """This is
a multi-line
string"""
print(multi_line)


# --------------------------------------------
# Advanced String Checking Methods
# --------------------------------------------

alpha_text = "Python"
numeric_text = "12345"
alnum_text = "Python123"
mixed_text = "Python 123"

print(alpha_text.isalpha())     # True
print(numeric_text.isnumeric()) # True
print(numeric_text.isdigit())   # True
print(alnum_text.isalnum())     # True
print(mixed_text.isalnum())     # False


# --------------------------------------------
# lower() vs casefold()
# --------------------------------------------

text = "PYTHON"
print(text.lower())
print(text.casefold())


# --------------------------------------------
# Alignment Methods
# --------------------------------------------

title = "Python"

print(title.center(20))
print(title.center(20, "-"))

print(title.ljust(15))
print(title.ljust(15, "*"))

print(title.rjust(15))
print(title.rjust(15, "*"))


# --------------------------------------------
# Zero Padding using zfill()
# --------------------------------------------

invoice_number = "42"
print(invoice_number.zfill(5))   # 00042
print("7".zfill(3))              # 007


# --------------------------------------------
# String Formatting (Professional Way)
# --------------------------------------------

salary = 50000

# f-string (Recommended)
print(f"Salary with commas: {salary:,}")

# format() method
print("Salary is {:,}".format(salary))


# --------------------------------------------
# Real-World Mini Examples
# --------------------------------------------

# Username Validation
username = "User123"

if username.isalnum():
    print("Valid Username")
else:
    print("Invalid Username")

# Formatting Order ID
order_id = "89"
formatted_order_id = order_id.zfill(6)
print("Order ID:", formatted_order_id)

# Case-Insensitive Comparison
user_input = "python"

if user_input.casefold() == "PYTHON".casefold():
    print("Match Found")


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------

# 1. Create a raw string for a file path.
# 2. Create an f-string to print name and salary.
# 3. Check whether a string contains only numbers.
# 4. Center a heading using '*'.
# 5. Format a number like 00089 using zfill().
# 6. Compare two strings ignoring case sensitivity.
