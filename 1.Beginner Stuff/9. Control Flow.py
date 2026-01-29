#====================================================
#               Control Flow in Python
#====================================================
# Control flow is used to control the execution of a program
# based on conditions.
# It helps the program decide:
# - what to execute
# - when to execute
# - which block to skip


#====================================================
#               if statement
#====================================================
# The if statement is used to execute a block of code
# only when the given condition is True.
# If the condition is False, the block will be skipped.

age = 18

if age >= 18:
    print("You are eligible to vote")

# Here:
# age >= 18 → condition
# If condition is True → print() runs
# If condition is False → nothing happens


#====================================================
#               if-else statement
#====================================================
# The if-else statement gives two paths:
# - if block runs when condition is True
# - else block runs when condition is False

marks = 35

if marks >= 40:
    print("You passed the exam")
else:
    print("You failed the exam")

# Only one block will execute at a time


#====================================================
#               if-elif-else statement
#====================================================
# Used when we have multiple conditions to check.
# Python checks conditions from top to bottom.
# The first True condition block will execute.

score = 78

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Fail")


#====================================================
#               Nested if statement
#====================================================
# When an if statement is written inside another if statement
# it is called a nested if.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Age restriction")

# First outer if is checked
# Then inner if is checked


#====================================================
#               match-case statement
#====================================================
# match-case is introduced in Python 3.10
# It is used as a replacement for switch-case
# in other programming languages.
# match compares a value and executes the matching case.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# case _ works like default in switch-case
# It runs when no case matches


#====================================================
#           match-case with strings
#====================================================
# match-case can also work with strings

browser = "chrome"

match browser:
    case "chrome":
        print("Opening Google Chrome")
    case "firefox":
        print("Opening Mozilla Firefox")
    case "edge":
        print("Opening Microsoft Edge")
    case _:
        print("Unsupported browser")


#====================================================
#           if-elif vs match-case
#====================================================
# Use if-elif when:
# - Conditions are complex
# - Logical operators (and, or, not) are needed

# Use match-case when:
# - Comparing a single variable
# - Fixed values are used
# - Code readability is important


#====================================================
#           Control flow with input()
#====================================================
# input() always returns a string
# So we convert it into int before comparison

choice = int(input("Enter a number between 1 to 3: "))

match choice:
    case 1:
        print("You selected option 1")
    case 2:
        print("You selected option 2")
    case 3:
        print("You selected option 3")
    case _:
        print("Invalid option")
