import random


def main():
    count = 0
    
    lives = 0
    lv = get_level()
    correct = 0
    while count <=9:
        try:
            count += 1
            x,y = generate_integer(lv)
            answer = input(f"{x} + {y} = ")
            if int(answer) == x+y:
                correct = correct + 1
                           

            while x+y!=int(answer) or lives==2:
                lives +=1
                
                print("EEE")
                answer = input(f"{x} + {y} = ")
                if lives <2 and int(answer)==x+y:
                    correct +=1
                    break
                elif lives==2:
                    print("EEE")
                    print(f"{x} + {y} = {x+y}")
                    lives = 0
                    break
        except:
            pass
    print(f"Score: {correct}")



def get_level():        # prompt for level and re-prompts if needed. returns : 1, 2 or 3
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1,2,3]:
                break           
            else:
                raise ValueError          
        except ValueError:
            pass
    return lvl



def generate_integer(level):    #returns integer with "level" digits or raises a ValueError if level is not 1,2 or 3
    
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
   
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    
    return x, y


main()