#====================================================
#               while loop in Python
#====================================================
# The while loop is used to execute a block of code repeatedly as long as a given condition is True.
#
# If the condition becomes False, the loop stops.


#====================================================
#               Syntax of while loop
#====================================================
# while condition:
#     code block
#
# NOTE:
# - condition must return True or False
# - indentation is very important


#====================================================
#               Basic Example
#====================================================
# Print numbers from 1 to 5

count = 1

while count <= 5:
    print(count)
    count = count + 1

# Flow:
# 1. count = 1
# 2. condition → count <= 5 (True)
# 3. print count
# 4. increment count
# 5. repeat until condition becomes False


#====================================================
#               Infinite while loop
#====================================================
# A loop that never stops is called an infinite loop.
# This happens when the condition always remains True.

# Example (DO NOT RUN THIS):
# while True:
#     print("This will run forever")

# To stop an infinite loop, we must:
# - change the condition
# - or use break statement


#====================================================
#               while loop with user input
#====================================================
# Take input until the correct password is entered

password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter password: ")

print("Access granted")


#====================================================
#               while loop with break
#====================================================
# break is used to exit the loop immediately

num = 1

while num <= 10:
    if num == 6:
        break
    print(num)
    num = num + 1

# Output: 1 2 3 4 5


#====================================================
#               while loop with continue
#====================================================
# continue skips the current iteration and moves
# to the next one

num = 0

while num < 5:
    num = num + 1
    if num == 3:
        continue
    print(num)

# Output: 1 2 4 5


#====================================================
#               while loop with else
#====================================================
# The else block executes when the loop ends normally
# (not terminated by break)

num = 1

while num <= 3:
    print(num)
    num = num + 1
else:
    print("Loop completed successfully")


#====================================================
#               Common mistakes (IMPORTANT)
#====================================================
# 1. Forgetting to update the condition variable
#    → causes infinite loop
#
# 2. Wrong indentation
#    → causes error or unexpected behavior
#
# 3. Using while when for loop is better
#
# Always check your condition carefully


#====================================================
#               Real-world use cases
#====================================================
# 1. Login system
# 2. Menu driven programs
# 3. Retry mechanism
# 4. Games (waiting for user action)


#====================================================
#               Summary
#====================================================
# - while loop runs based on condition
# - condition must change to avoid infinite loop
# - break and continue control loop execution
