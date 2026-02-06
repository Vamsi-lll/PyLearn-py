#====================================================
#          LOOP CONTROL STATEMENTS IN PYTHON
#====================================================

# Loop control statements are used to control
# the execution flow of loops.

# Python provides three loop control statements:
# 1. break
# 2. continue
# 3. pass


#====================================================
#                 break STATEMENT
#====================================================

# The break statement is used to terminate the loop immediately
# when a specific condition is met.

# Example:
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Output:
# 1 2 3 4


# Real-life example:
# Stop searching once the item is found

items = ["pen", "book", "laptop", "phone"]

for item in items:
    if item == "laptop":
        print("Item found!")
        break
    print("Checking:", item)


#====================================================
#               continue STATEMENT
#====================================================

# The continue statement skips the current iteration
# and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output:
# 1 2 4 5


#====================================================
#                 pass STATEMENT
#====================================================

# The pass statement does nothing.
# It is used as a placeholder when a statement is required
# syntactically but no action is needed.

# Example:
for i in range(1, 5):
    if i == 3:
        pass
    print(i)

# pass is commonly used while:
# - designing structure first
# - writing empty functions or loops
# - avoiding syntax errors during development


#====================================================
#           pass IN FUNCTION (example)
#====================================================

def future_feature():
    pass

# This function is empty now
# but can be implemented later


#====================================================
#           KEY DIFFERENCE SUMMARY
#====================================================

# break    -> exits the loop completely
# continue -> skips current iteration
# pass     -> does nothing (placeholder)
