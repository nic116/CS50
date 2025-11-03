
import random

#main function:
    # input level
def main():
    
    lvl = input("Level: ")
    while lvl.isnumeric() == False or int(lvl)<1 :
        lvl = input("Level: ")
        
    # pass level to the function where
    result = get_game(int(lvl))
    print(result)


def get_game(lv):
    
    n = random.randint(1,lv)
    while True:
        guess = input("Guess: ")
        while guess.isnumeric() == False or int(guess)<=0:#or int(guess)>lv:
            guess = input("Guess: ")
        if int(guess)!= n and int(guess)<n:
            print("Too small!")
        elif int(guess) != n and int(guess)>n:
            print("Too large!")
        else:
            False
            return "Just right!"
main()