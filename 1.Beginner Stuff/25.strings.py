
# ============================================
# String Data Type in Python
# ============================================

# --------------------------------------------
# What is a String?
# --------------------------------------------
# A string is a sequence of characters used
# to represent text in Python.
# Strings are surrounded by quotes (' ', " ", or ''' ''')

# Example:
text = "Hello Python"


# --------------------------------------------
# Why do we need Strings?
# --------------------------------------------
# Strings are used to store:
# - Names
# - Messages
# - User input
# - File content
# - API data (JSON, text)

username = "admin"
message = "Welcome to Python"


# --------------------------------------------
# How to create a String
# --------------------------------------------

str1 = "Python"
str2 = 'Programming'
str3 = """This is
a multi-line
string"""

empty_string = ""


# --------------------------------------------
# Basic Operations on String
# --------------------------------------------

# Accessing characters using index
word = "Python"

print(word[0])   # P
print(word[3])   # h

# Length of string
print(len(word))  # 6

# String concatenation
first = "Hello"
second = "World"
result = first + " " + second
print(result)


# --------------------------------------------
# Immutability of String
# --------------------------------------------
# String is an IMMUTABLE data type
# Meaning: we cannot change characters directly

language = "Python"

# language[0] = "J"   ❌ This will raise an error

# Correct way:
language = "J" + language[1:]
print(language)


# --------------------------------------------
# Common Built-in String Methods
# --------------------------------------------

sentence = "  learn python programming  "

print(sentence.upper())       # convert to uppercase
print(sentence.lower())       # convert to lowercase
print(sentence.strip())       # remove extra spaces
print(sentence.replace("python", "java"))
print(sentence.split())       # split into list

# Checking content
print(sentence.startswith("learn"))
print(sentence.endswith("programming"))


# --------------------------------------------
# Mini Examples
# --------------------------------------------

# Example 1: User input cleanup
email = "  user@example.com  "
clean_email = email.strip()
print(clean_email)

# Example 2: Word count
text_data = "python is easy to learn"
words = text_data.split()
print(len(words))

# Example 3: Simple formatting
greeting = "Hello"
platform = "Python"
print(greeting + " Welcome to " + platform)


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a string and print its length.
# 2. Access the first and last character of a string.
# 3. Convert a string to uppercase.
# 4. Remove extra spaces from a string.
# 5. Split a sentence into words.
# 6. Why are strings immutable?
