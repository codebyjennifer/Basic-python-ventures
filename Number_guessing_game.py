import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
num = random.randint(1,100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempt1 = 10
attempt2 = 5

def easy_level(a,b):

    if a != b:
        global attempt1
        attempt1 -= 1
        print(f"You have {attempt1} attempts remaining to guess the number.")
def hard_level(a,b):


    if a != b:
        global attempt2
        attempt2 -= 1
        print(f"You have {attempt2} attempts remaining to guess the number.")

def game():
    while attempt1 != 0 and attempt2 != 0:
        guess = int(input("Make a guess: "))
        if level == "easy":
            easy_level(a=num, b=guess)
        elif level == "hard":
            hard_level(a=num, b=guess)
        else:
            print("There is no such option. Refresh and try again!")
            break
        if guess < num:
            print("Too low!\nGuess again.")

        elif guess > num:
            print("Too high!\nGuess again.")

        elif guess == num:
            print("Congratulations! You won!")
            break

game()







