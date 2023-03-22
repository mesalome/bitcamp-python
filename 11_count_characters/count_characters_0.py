def main():
    text = input("input your word\n")
    characters = count(text)
    output(text, characters)


def count(txt):
    return len(txt)

def output(txt, number):
    if number == 0:
        print("You must enter input")
    else:
        print(txt + " has " +str(number)+ " characters")

main()