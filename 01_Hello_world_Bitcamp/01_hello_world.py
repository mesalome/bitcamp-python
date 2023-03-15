#task 1
#Asks and saves your name
n = input("What is your name? ")

# removes spaces from the begining and the end, every word is capitalized
n = n.strip().title()

# creates list of words
n = n.split()

#joins list items into a sentence and separates with space 
n = " ".join(n)

# #prints your name, removes spaces from the begining and the end, every word is capitalized
print("Hello, " + n +", Nice to meet you!" )
