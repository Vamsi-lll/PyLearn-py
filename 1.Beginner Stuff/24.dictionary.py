# ============================================
# Dictionary Collection Type in Python
# ============================================

# --------------------------------------------
# What is a Dictionary?
# --------------------------------------------
# A dictionary is a collection data type in Python
# used to store data in the form of KEY : VALUE pairs.
# Each key value pair together called as ITEM.
# Each key is used to access its corresponding value.

# Example:
my_dict = {
    "name": "pylearn",
    "version": 1
}


# --------------------------------------------
# Why do we need a Dictionary?
# --------------------------------------------
# Dictionary is used when data has a relationship.
# Example: user details, configuration, database records.

student = {
    "name": "alex",
    "age": 21,
    "course": "Python"
}


# --------------------------------------------
# How to create a Dictionary
# --------------------------------------------
# Dictionaries are created using curly braces {}

empty_dict = {}

data = {
    "language": "Python",
    "year": 2026,
    "is_popular": True
}


# --------------------------------------------
# Basic Operations on Dictionary
# --------------------------------------------

# Accessing values using keys
print(data["language"])     # Python
print(data["year"])         # 2026

# Adding a new key-value pair
data["creator"] = "Guido"
print(data)

# Updating a value
data["year"] = 2025
print(data)

# Removing a key-value pair
data.pop("is_popular")
print(data)

# Length of dictionary
print(len(data))


# --------------------------------------------
# Mutability of Dictionary
# --------------------------------------------
# Dictionary is MUTABLE
# Meaning: we can add, update, or delete values

config = {
    "theme": "dark",
    "debug": True
}

config["debug"] = False
print(config)


# --------------------------------------------
# Common Built-in Dictionary Methods
# --------------------------------------------

info = {
    "name": "Python",
    "type": "Programming Language"
}

print(info.keys())      # get all keys
print(info.values())    # get all values
print(info.items())     # get key-value pairs

# Safe access using get()
print(info.get("name"))
print(info.get("version"))  # returns None (no error)


# --------------------------------------------
# Mini Examples
# --------------------------------------------

# Example 1: User profile
user = {
    "username": "admin",
    "email": "admin@example.com",
    "active": True
}

# Example 2: Product details
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000
}

# Example 3: Nested dictionary
employee = {
    "id": 1,
    "details": {
        "name": "Ravi",
        "role": "Developer"
    }
}


# --------------------------------------------
# Practice Questions (Do NOT write code now)
# --------------------------------------------
# 1. Create a dictionary with 5 key-value pairs.
# 2. Access a value using its key.
# 3. Add a new key-value pair to an existing dictionary.
# 4. Update an existing value.
# 5. Remove a key from a dictionary.
# 6. What happens if you access a key that does not exist?
# 7. What is the difference between list and dictionary?
