

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
rules = input('''1.The game consists of five different stages.
2.Choose all right options to win the game.
3.10 points will be awarded for choosing each correct option.
4.The game consists of total 50 points.
5.All the best!
6.Press "enter" to continue. ''')
score = 0
direction = input("Choose which way to go. left or right? ").lower()
if direction == "left":
    score+=10
    swim_or_wait1 = input('You\'ve found a lake with deadly piranhas.')
    swim_or_wait2 = input('Type "wait" if you wanna wait for the boat'
                          ' or "swim" if you wanna swim across.').lower()
    if swim_or_wait2 == "swim":
        print("The piranhas bit you badly on your butt. Game Over!")
        print(f'Your final score is {score}.')
    elif swim_or_wait2 == "wait":
        score+=10
        input("You have reached to a small hut unharmed.")
        input('There is an old lady in front of you.')
        truth_or_lie1 = input("The old lady is asking if you are looking for the treasure? ")
        truth_or_lie2 = input("Type 'Y' for yes and 'N' for no. ").lower()
        if truth_or_lie2 == "n":
            print("The old lady knew that you were there for the treasure."
                  "She cursed you for lying. Game over!")
            print(f'Your final score is {score}.')
        elif truth_or_lie2 == "y":
            score+=10
            input("The old lady is impressed by your honesty. ")
            follow1 = input('She is asking you to follow her. ')
            follow2 = input('Type "Y" to follow her and "N" to run away.').lower()
            if follow2 == "n":
                print("You ran away but on the way you were bitten by a "
                      "poisonous snake. Game Over!")
                print(f'Your final score is {score}.')


            elif follow2 == "y":
                score+=10
                print("The lady said:")
                input("There are three doors in front of you.")
                hint = input('''Which door would you choose? Red, Blue or Yellow?" '
'Do you want a hint?
Type "Y" for yes and "N" for no. ''').lower()
                if hint == "y":
                   input("HINT: The gold shines.")
                   door = input("Which door would you choose? Red, Blue or Yellow? ").lower()
                elif hint == "n":
                    door = input("Which door would you choose? Red, Blue or Yellow? ").lower()
                else:
                    print("You entered the wrong input.")
                if  door == "red":
                    print("You were attacked by Rhinos. Game Over!")
                    print(f'Your final score is {score}.')
                elif door == "blue":
                    print("A blue whale ate you. Game over!")
                    print(f'Your final score is {score}.')
                elif door == "yellow":
                    score+=10
                    print('''It was the spark of the gold coins.
Congratulations! 
You found the treasure.
You Won!''')
                    print(f'Your final score is {score}!!')

                else:
                    print("There is no such door. Game Over!")
                    print(f'Your final score is {score}.')

            else:
                print("You entered the wrong input.")


    else:
        print("You entered the wrong input.")
elif direction == "right":
    input("You came across a tiny orchard in the middle of the forest.")
    input("The orchard keeper is glaring at you.")
    orchard_keeper = input('''Type "Y" to ask him about the treasure
or "N" to ignore and continue to move forward.\n''').lower()
    if orchard_keeper == "y":
        input("He was surprised to hear about the hidden treasure.")
        want_help = input('''Type "help" to ask him to help you 
or "joking" to tell him that there is no treasure.\n''').lower()
        if want_help == "help":
            input("The orchard keeper agreed to do so.")
            input('''You both decided to move together to the Helphredian cliff
as its known for its mystical happenings.''')
            input('''On the way, you both became really good friends
and you told him everything you knew about the treasure. ''')
            input(" That night, you both stayed in a dark mystical cave.")
            input('''Do you wanna betray your new friend (the orchard keeper)
and take all his stuff and search take the treasure alone?''')
            betray = input('Type "Y" for yes and "N" for no.\n').lower()
            if betray == "n":
                print('''The next morning as you woke up,
your new friend betrayed you. he took all of your stuff
and went to search for the treasure alone.
You lost. Game Over!!''')
            elif betray == "y":
                input("You went to search for the treasure alone.")
                print('''On the way, you were bitten by a whole bunch of hyena bees.
You needed help but nobody was there to help you.
You lost. Game Over!''')
            else:
                print("Wrong input!")
        elif want_help == "joking":
            input("The orchard keeper is suspecting you.")
            input("He thinks that you are lying.")
            input("He is very poor and is requesting you to tell him the truth.")
            tell_truth = input('Type "Y" to tell him the truth or "N" to lie.\n').lower()
            if tell_truth == "y":
                input("He thanked you and requested you to let him allow him to join you in the mission.")
                join = input('Type "Y" to agree or "N" to deny.\n').lower()
                if join == "y":
                    input('''You both decided to move together to the Helphredian cliff
                             as its known for its mystical happenings.''')
                    input('''On the way, you both became really good friends
                        and you told him everything you knew about the treasure. ''')
                    input(" That night, you both stayed in a dark mystical cave.")
                    input('''Do you wanna betray your new friend (the orchard keeper)
                            and take all his stuff and search take the treasure alone?''')
                    betray = input('Type "Y" for yes and "N" for no.\n').lower()
                    if betray == "n":
                        input('''The next morning, on the way to the cliff, 
                                you both reached a small hut.''')

                        input("There was an old lady in the hut.")
                        truth_or_lie1 = input("The old lady is asking if you are looking for the treasure? ")
                        truth_or_lie2 = input("Type 'Y' for yes and 'N' for no. ").lower()
                        if truth_or_lie2 == "n":
                            print("The old lady knew that you were there for the treasure."
                                  "She cursed you for lying. Game over!")
                            print(f'Your final score is {score}.')
                        elif truth_or_lie2 == "y":
                            score += 10
                            input("The old lady is impressed by your honesty. ")
                            follow1 = input('She is asking you to follow her. ')
                            follow2 = input('Type "Y" to follow her and "N" to run away.').lower()
                            if follow2 == "n":
                                print("You ran away but on the way you were bitten by a "
                                      "poisonous snake. Game Over!")


                            elif follow2 == "y":
                                score += 10
                                print("The lady said:")
                                input("There are three doors in front of you.")
                                hint = input('''Which door would you choose? Red, Blue or Yellow?" '
                                                'Do you want a hint?
                                                Type "Y" for yes and "N" for no. ''').lower()
                                if hint == "y":
                                    input("HINT: The gold shines.")
                                    door = input("Which door would you choose? Red, Blue or Yellow? ").lower()
                                elif hint == "n":
                                    door = input("Which door would you choose? Red, Blue or Yellow? ").lower()
                                else:
                                    print("You entered the wrong input.")
                                if door == "red":
                                    print("You were attacked by Rhinos. Game Over!")
                                    print(f'Your final score is {score}.')
                                elif door == "blue":
                                    print("A blue whale ate you. Game over!")
                                    print(f'Your final score is {score}.')
                                elif door == "yellow":
                                    score += 10
                                    print('''It was the spark of the gold coins.
                                         Congratulations! 
                                         You found the treasure.
                                         It was the result of showing kindness and honesty.
                                         You Won!''')
                                    print(f'Your final score is {score}!!')
                                else:
                                    print("There is no such door.")
                    elif betray == "y":
                        input("You went to search for the treasure alone.")
                        print('''On the way, you were bitten by a whole bunch of hyena bees.
                                   You needed help but nobody was there to help you.
                                   You lost. Game Over!''')
                    else:
                        print("You entered the wrong input!")
                elif join == "n":
                    input("You went to search for the treasure alone.")
                    print('''On the way, you were bitten by a whole bunch of hyena bees.
                            You needed help but nobody was there to help you.
                            You lost. Game Over!''')
            elif tell_truth == "n":
                input("You went to search for the treasure alone.")
                print('''On the way, you were bitten by a whole bunch of hyena bees.
                                        You needed help but nobody was there to help you.
                                        You lost. Game Over!''')

    elif orchard_keeper == "n":
        input("You went to search for the treasure alone.")
        print('''On the way, you were bitten by a whole bunch of hyena bees.
        You needed help but nobody was there to help you.
        You lost. Game Over!''')

else:
    print("You entered the wrong input.")


