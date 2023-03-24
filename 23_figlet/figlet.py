from pyfiglet import Figlet
import sys


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--front":
        if sys.argv[2] in Figlet.getFonts(Figlet()):
            f = Figlet(font = sys.argv[2])
            print (f.renderText(input("Input: ")))
        else:
            sys.exit("error message")
    else:
        sys.exit("error message")
    
else: 
    f = Figlet(font='5lineoblique')
    print (f.renderText(input("Input: ")))