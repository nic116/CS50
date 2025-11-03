from pyfiglet import Figlet
import sys
from random import choice


figlet = Figlet()

accpt_format = ["-f", "--font"]

def main():
    
 
    if len(sys.argv) == 3:
        if sys.argv[2] not in figlet.getFonts() or sys.argv[1] not in accpt_format:
                sys.exit("Invalid usage")
        else:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input("Input: ")))
    elif len(sys.argv) == 1:
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(input("Input: ")))
    else:
        sys.exit("Invalid usage")
         
      

main()