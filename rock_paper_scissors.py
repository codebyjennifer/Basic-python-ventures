import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
random_choice_list = [rock, paper, scissors]
random_choice = random.choice(random_choice_list)
choice = int(input("Type what do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n "))
if choice == 0:
    print("user's choice: " + rock)
    print("computer's choice: " + random_choice)
    if random_choice == rock:
        print('tie')
    elif random_choice == paper:
        print("you lost")
    elif random_choice == scissors:
        print('you won')
elif choice == 1:
    print("user's choice: " + paper)
    print("computer's choice: " + random_choice)
    if random_choice == rock:
        print('you won')
    elif random_choice == paper:
        print("tie")
    elif random_choice == scissors:
        print('You lost')
elif choice == 2:
    print("user's choice: " + scissors)
    print("computer's choice: " + random_choice)
    if random_choice == rock:
        print('you lost')
    elif random_choice == paper:
        print("you won")
    elif random_choice == scissors:
        print('tie')
else:
    print("There is no such choice")





