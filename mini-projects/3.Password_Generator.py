import random
import string


def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    letters = random.choice(string.ascii_letters)
    numbers = random.choice(string.digits)
    symbols = random.choice(string.punctuation)

    remaining_length = length - 3
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = letters + numbers + symbols

    for _ in range(remaining_length):
        password += random.choice(all_characters)

    password_list = list(password)
    random.shuffle(password_list)

    return "".join(password_list)


print("Professional Password Generator")
length = int(input("Enter password length: "))

result = generate_password(length)
print("Generated Password:", result)
