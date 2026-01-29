#====================================================
#               Control Flow in Python
#====================================================
# Control flow is used to control the execution of a program
# based on conditions.
# Python provides:
# 1. if
# 2. if-else
# 3. if-elif-else
# 4. match-case (similar to switch-case)


#====================================================
#               if statement
#====================================================

age = 18

if age >= 18:
    print("You are eligible to vote")


#====================================================
#               if-else statement
#====================================================

marks = 35

if marks >= 40:
    print("You passed the exam")
else:
    print("You failed the exam")


#====================================================
#               if-elif-else statement
#====================================================

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
#               Nested if
#====================================================

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID is required")
else:
    print("Age restriction")


#====================================================
#               match-case statement
#====================================================
# match-case is introduced in Python 3.10
# It works similar to switch-case in other programming languages
# match checks the value and executes the matching case

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


#====================================================
#           match-case with strings
#====================================================

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
#           match-case vs if-elif
#====================================================
# Use match-case when:
# - You are comparing a single variable
# - You have fixed values
# - Code readability matters

# Use if-elif when:
# - Conditions are complex
# - Logical operators are required


#====================================================
#           Input with Control Flow
#====================================================

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
