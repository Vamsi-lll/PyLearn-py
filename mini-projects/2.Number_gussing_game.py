import random

comp_num = random.randint(0, 99)
guess_status = True

while guess_status:
    user_guess = int(input("Guess the number between 0 to 99 = "))
    
    if comp_num == user_guess:
        print("You guessed this right!")
        guess_status = False
      
    elif user_guess > comp_num:
        print("Your number is too high...")
    
    else:
        print("Your number is too low...")
