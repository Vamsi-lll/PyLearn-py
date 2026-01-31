#================================================
#          Python Keywords (Complete List)
#================================================
# Keywords are reserved words in Python.
# They have predefined meanings and cannot be
# used as variable names, function names, or class names.


#================================================
#          List of All Python Keywords
#================================================

#  1. False     → Boolean false value
#  2. None      → Represents no value
#  3. True      → Boolean true value

#  4. and       → Logical AND operator
#  5. or        → Logical OR operator
#  6. not       → Logical NOT operator

#  7. if        → Conditional statement
#  8. elif      → Else-if condition
#  9. else      → Executes when if condition is false

# 10. for       → Looping statement
# 11. while     → Looping statement
# 12. break     → Terminates the loop
# 13. continue  → Skips current iteration
# 14. pass      → Does nothing (placeholder)

# 15. in        → Membership operator
# 16. is        → Identity operator

# 17. def       → Function definition
# 18. return    → Returns value from function
# 19. lambda    → Anonymous function

# 20. class     → Class definition
# 21. del       → Deletes an object
# 22. global    → Declares global variable
# 23. nonlocal  → Declares non-local variable

# 24. try       → Exception handling
# 25. except    → Handles exception
# 26. finally   → Always executes
# 27. raise     → Raises an exception
# 28. assert    → Debugging check

# 29. import    → Imports a module
# 30. from      → Imports specific part of module
# 31. as        → Alias for module or keyword

# 32. with      → Context manager
# 33. yield     → Returns value from generator

# 34. async     → Asynchronous programming
# 35. await     → Waits for async result

# 36. match     → Pattern matching (Python 3.10+)
# 37. case      → Used inside match-case

# NOTE:
# match and case are sometimes counted separately
# depending on Python version, which is why you may
# see 35–37 keywords mentioned in different places.


#================================================
#          Example: Invalid Keyword Usage
#================================================
# The below lines will cause errors 
# if = 10
# for = "python"
# class = "test"


#================================================
#      Python Keywords – Practical Example
#================================================
# Python provides a built-in module called `keyword`
# which helps us work with Python keywords


#================================================
#      Importing keyword module
#================================================
import keyword


#================================================
#      Display all Python keywords
#================================================
# keyword.kwlist returns a list of all keywords

print("List of all Python keywords:\n")
print(keyword.kwlist)

# Total number of keywords
print("\nTotal number of keywords:", len(keyword.kwlist))


#================================================
#      Check whether a word is a keyword or not
#================================================
# keyword.iskeyword() returns:
# True  → if the word is a keyword
# False → if the word is NOT a keyword

word = input("\nEnter a word to check whether it is a keyword: ")

if keyword.iskeyword(word):
    print(f"'{word}' is a Python keyword")
else:
    print(f"'{word}' is NOT a Python keyword")


