# ROCK, PAPER, SCISSORS


## Beginning 
I'm creating a software which will play "Rock, Paper, Scissors" with a user. 
To do this I need:
1. user to be able to input their choice
2. computer generating random choice
3. outputting both choice 
4. outputting winner

    ### rock, paper, scissors Rules

        * Rock beats Scissors
        * Paper beats Rock
        * Scissors beats Paper

## Advancements
to advance software I can add additional functions:
1. ask user after first game if they want to keep playing
2. quit game if they press anything other than Y
3. make game much more COMPLICATED by adding additional actions: Lizard and Spock

    ### rock, paper, scissors, lizard, Spock Rules

        * Rock beats Scissors
        * Rock beats Lizard
        * Paper beats Rock
        * Paper beats Spock
        * Scissors beats Paper
        * Scissors beats Lizard
        * Lizard beats Paper
        * Lizard beats Spock
        * Spock beats Rock
        * Spock beats Scissors

        <!-- for a better visualization check diagram: -->
        ![image](https://upload.wikimedia.org/wikipedia/en/c/cc/Rock_paper_scissors_lizard_spock.png)

## Coding Process
### beginning version 1.0
1. for the beginning version I only need one additional library: __Random__  
    *   __Random__ for computer's random action
2. three different function
    * user_input() - which will get action and change it into 0, 1, or 2
    * computer_input() - which will generate random number 0, 1, or 2
    * match(user_input, computer_input) - function with two parameters to decide winner according to Rules

### advanced version
#### advanced version 2.0
1. for the advanced version I need to add library: __Re__
    * __Re__ for checking user's input and if it maches "Y" or "y" to exit game
2. while loop to keep playing until user exits on their choice

#### advanced version 2.1
1. because code will became way harder to read with additional actions, I'll add class __IntEnum__ from __enum__
    which will make code readable 
2. 