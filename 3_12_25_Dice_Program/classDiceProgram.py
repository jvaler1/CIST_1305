# Function Program:
# We want our program to roll dice. 
# We want it to give us a result.
# If sum of dice is 7 or 11, you lose.
# If the roll is not a 7 or 11, you get the choice to roll again.
# If both dice are the same, print "Congratulations, you got a hard {1 through 6}".

import random

def main():

    # Loop to allow for multiple rolls
    loop = True
    while loop:

        # Generate new dice rolls
        dice1, dice2 = rollDice()

        # Evaluate the dice rolls
        loss, double, diceSum = eval(dice1, dice2)

        # Determines path of action based on eval outcome
        if not loss and not double:
            loopQuery = input(f"You rolled a {dice1} and {dice2} totaling {diceSum}, do you want to roll again? Y/N: ")
            if loopQuery == "Y":
                loop = True
            elif loopQuery == "N":
                loop = False
            else:
                print("Error: Invalid input.")
                break
        # If double, print outcome and end loop
        elif double:
            print(f"Congratulations, your roll of a {dice1} and a {dice2} is a double!")
            loop = False
        # If loss, print outcome and end loop
        else:
            loop = False
            print(f"You rolled a {diceSum}, you lose...")

# Uses random module to generate dice rolls
def rollDice():
    dice1 = random.randrange(1,6)
    dice2 = random.randrange(1,6)
    return(dice1, dice2)

# Evaluates dice roll for immediate win/loss as well as doubles
def eval(dice1, dice2):
    # Checks for 7 or 11 total, which loses
    diceSum = dice1 + dice2
    if diceSum == 7 or diceSum == 11:
        loss = True
    else:
        loss = False

    # Checks for doubles
    if dice1 == dice2:
        double = True
    else:
        double = False

    return(loss, double, diceSum)

main()
