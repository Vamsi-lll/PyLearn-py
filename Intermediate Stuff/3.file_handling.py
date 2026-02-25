# ============================================
# File Handling in Python
# ============================================


# --------------------------------------------
# What is File Handling?
# --------------------------------------------
# File handling allows us to:
# - Read data from files
# - Write data into files
# - Store information permanently


# --------------------------------------------
# Why Do We Need File Handling?
# --------------------------------------------
# In real-world applications:
# - Store user data
# - Read configuration files
# - Process logs
# - Generate reports
# - Work with CSV, text, JSON files


# --------------------------------------------
# Opening a File
# --------------------------------------------

# Syntax:
# open("filename", "mode")

# Common Modes:
# "r"  -> Read (default)
# "w"  -> Write (overwrites file)
# "a"  -> Append (adds content)
# "x"  -> Create new file
# "b"  -> Binary mode
# "t"  -> Text mode (default)


# --------------------------------------------
# Reading from a File
# --------------------------------------------

# Example file: sample.txt (create this file manually)

# Method 1: read()
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


# Method 2: readline()
file = open("sample.txt", "r")
line = file.readline()
print(line)
file.close()


# Method 3: readlines()
file = open("sample.txt", "r")
lines = file.readlines()
print(lines)
file.close()


# --------------------------------------------
# Writing to a File
# --------------------------------------------

# "w" mode (overwrites existing content)
file = open("output.txt", "w")
file.write("Hello Python\n")
file.write("File Handling Example\n")
file.close()


# --------------------------------------------
# Appending to a File
# --------------------------------------------

file = open("output.txt", "a")
file.write("This line is appended.\n")
file.close()


# --------------------------------------------
# Using 'with' Statement (Recommended Way)
# --------------------------------------------

# Automatically closes the file

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)


# --------------------------------------------
# Real-World Mini Examples
# --------------------------------------------

# Example 1: Save User Input to File
user_name = "Alex"

with open("users.txt", "a") as file:
    file.write(user_name + "\n")


# Example 2: Count Words in a File
with open("sample.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Total words:", len(words))


# Example 3: Copy Content from One File to Another
with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)


# --------------------------------------------
# Important Notes
# --------------------------------------------
# - Always close files after opening
# - Prefer using 'with' statement
# - Be careful with "w" mode (it deletes existing content)


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a file and write 5 lines into it.
# 2. Read a file and print its content line by line.
# 3. Append new data to an existing file.
# 4. Count number of characters in a file.
# 5. Copy content from one file to another.
# 6. What is the difference between "w" and "a" mode?
