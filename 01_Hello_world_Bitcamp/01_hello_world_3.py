
# task 3
import random


#sentence starters
myGreetingStarts = ["Hello ", "Hi ", "Good morning ", "Good evening "]

#sentence finishers
myGreetingFinishes = [", it's nice to meet you", ", I'm so pleased to meet you", ", how loveley to see you here"]

#asks and saves name
n = input("What's your name? ")

#removes spaces from the beginning and end, capitalizes first letters
n = n.strip().title()

#creates list of words
n = n.split()

#joins words from list into a string, separates with space
n = " ".join(n)

#choosed random start and end
start = random.choice(myGreetingStarts) 
end = random.choice(myGreetingFinishes)

#prints random greeting with input name  
print(start + n + end)

