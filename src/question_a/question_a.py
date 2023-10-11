#write functions here, don't add input('') statements here!
import random

def test_config():
    return True

def get_random_number():
    num = random.randrange(1,6)
    return int(num)

def number_guessing_game():
    guess = int(input(" guess a number between 1 - 5: \n"))
    num = get_random_number()
    while guess != num:
        if guess != num:
            while guess < 1 or guess > 5:
                guess = int(input("please select a number 1 - 5:\n"))

            guess = int(input(" Guess again: \n"))
    
    print(f"congrats! you guessed right! the number was {num}")
    cont()
            
def cont():
    answer = input("Would you like to guess again?\n Type 'Y' for Yes\n Type 'N' to Exit:\n")
    while answer.upper() != 'N':
        if answer.upper()== 'Y':
            number_guessing_game()
        else:
            answer = input("Please select 'Y' or 'N':\n")
    print("Program exited")
    exit()
