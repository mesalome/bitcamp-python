import random
import re
    
def main():
    #after first game user will be asked if they want to keep playing or quit
    #loop will be over if user press any other character than Y
    while True:
        if match(user_input(), computer_input()) != None:
            print(match(user_input(), computer_input()))
        question = input("If you want to keep playing press Y. To quit press any other character ")
        if re.match("^[Y]{1}$", question, re.IGNORECASE):
            continue
        else:
            break
        # if re.match("^[^y]$", question, re.IGNORECASE):
        #     break

# fanction changes user input into numbers
# rock is 0
# paper is 1
# scissors is 2

def user_input():
    myinput = input("Rock, Paper or Scissors?: ").lower()
    if myinput == "rock":
        return 0
    if myinput == "paper":
        return 1
    if myinput == "scissors":
        return 2

# computer's action is chosen randomly from list [0, 1, 2]

def computer_input():
    return random.choice(range(3))

# def matching_rules():

    # Rock beats Scissors
    # Paper beats Rock
    # Scissors beats Paper


def match(user_input, computer_input):
    draws = ["Rock", "Paper", "Scissors"]

#if user writes something other than given 3 actions, they will be notified to fix it.
    try:
        #user's choice output on screen
        print("User played: ", draws[user_input])

        #computer's choice output on screen
        print("Computer played ", draws[computer_input])
        if user_input == computer_input:
            return "It's draw"
        elif user_input == 0:
            if  computer_input == 1:
                return "You Lost!, Papper beats Rock"
            elif computer_input == 2:
                return "You Won!, Rock beats Scissors"
        elif user_input == 1: 
            if computer_input == 0:
                return "You Won, Papper beats Rock"
            elif computer_input == 2:
                return "You Lost, Scissors beats Paper"
        elif user_input == 2:
            if computer_input == 1:
                return "You Won, Scissors beats Paper"
            elif computer_input == 0:
                return "You Lost, Rock beats Scissors"
    except TypeError:
        print("Please write one of three possible actions")
        pass
    
    

if __name__ == "__main__":
    main()