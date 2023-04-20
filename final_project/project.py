import random
import re
from enum import IntEnum
    
#this class makes code easier to read
class Shoot(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

#if user writes something other than given 3 actions, they will be notified to fix it.
#after first game user will be asked if they want to keep playing or quit
#loop will be over if user press any other character than Y
def main():
    while True:
        try:
            userInput = user_input()
            computerInput = computer_input()
            match_shoots_output(userInput, computerInput)
        except TypeError:
            print("Please write one of three possible actions")
        else:
            result = match_result(userInput, computerInput)
            print(result)
            question = input("If you want to keep playing press Y. (To quit press any other character) ")
            if re.match("^[Y]{1}$", question, re.IGNORECASE):
                continue
            else:
                break

# fanction changes user input into numbers which now are called using Shoot class
# rock is 0, same as Shoot.Rock
# paper is 1 same as Shoot.Paper
# scissors is 2 same as Shoot.Scissors
def user_input():
    myinput = input("Rock, Paper or Scissors?: ").lower()
    if myinput == "rock":
        return Shoot.Rock
    if myinput == "paper":
        return Shoot.Paper
    if myinput == "scissors":
        return Shoot.Scissors


# computer's action is chosen randomly from list [0, 1, 2]
def computer_input():
    return random.choice(range(len(Shoot)))


#basic matching rules
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper

def match_shoots_output(user_input, computer_input):
    shoots = ["Rock", "Paper", "Scissors"]
    #user's choice output on screen
    print("User played: ", shoots[user_input])
    #computer's choice output on screen
    print("Computer played ", shoots[computer_input])

def match_result(user_input, computer_input):
    if user_input == computer_input:
        return "It's a tie"
    elif user_input == Shoot.Rock:
        if  computer_input == Shoot.Paper:
            return "You Lost!, Papper beats Rock"
        elif computer_input == Shoot.Scissors:
            return "You Won!, Rock beats Scissors"
    elif user_input == Shoot.Paper: 
        if computer_input == Shoot.Rock:
            return "You Won, Papper beats Rock"
        elif computer_input == Shoot.Scissors:
            return "You Lost, Scissors beats Paper"
    elif user_input == Shoot.Scissors:
        if computer_input == Shoot.Paper:
            return "You Won, Scissors beats Paper"
        elif computer_input == Shoot.Rock:
            return "You Lost, Rock beats Scissors"
    
    

if __name__ == "__main__":
    main()