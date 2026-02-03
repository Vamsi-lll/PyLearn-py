#====================================================
#               Loops in Python
#====================================================
# In programming, we often need to repeat the same
# task multiple times.
# Writing the same code again and again is not a
# good practice.
#
# To solve this problem, Python provides LOOPS.


#====================================================
#               What are Loops?
#====================================================
# A loop is a control structure that allows us to
# execute a block of code repeatedly until a
# certain condition is satisfied.
#
# In simple words:
# Loops help us to avoid repetition of code.


#====================================================
#               Why do we need Loops?
#====================================================
# Without loops:
# We would need to write the same code multiple times.
#
# With loops:
# - Code becomes shorter
# - Code becomes cleaner
# - Code becomes easier to maintain


#====================================================
#               Real-world examples of Loops
#====================================================
# 1. Attendance in a class
# 2. Printing numbers from 1 to 100
# 3. Reading multiple user inputs
# 4. Checking marks of multiple students
# 5. Repeating a task until a condition is met


#====================================================
#               Types of Loops in Python
#====================================================
# Python mainly provides two types of loops:
#
# 1. while loop
# 2. for loop
#
# (We will study each of them in detail in
# separate files)


#====================================================
#               while loop (overview)
#====================================================
# The while loop runs as long as a condition is True.
#
# Syntax:
# while condition:
#     code block
#
# Example (just for understanding):

count = 1
while count <= 3:
    print("Hello from while loop")
    count = count + 1


#====================================================
#               for loop (overview)
#====================================================
# The for loop is mainly used to iterate over
# a sequence like:
# - list
# - tuple
# - string
# - range
#
# Example (just for understanding):

for i in range(3):
    print("Hello from for loop")


#====================================================
#               When to use which loop?
#====================================================
# Use while loop when:
# - You do not know how many times the loop will run
# - The loop depends on a condition
#
# Use for loop when:
# - You know how many times the loop should run
# - You are iterating over a collection


#====================================================
#               Important note for beginners
#====================================================
# - Loops work closely with conditions
# - Indentation is very important in loops
# - Wrong indentation will cause errors
#
# We will go deep into:
# - while loop in while_loop.py
# - for loop in for_loop.py
