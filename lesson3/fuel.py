
def main():
    f = get_int(input("Fraction: "))
    if f != None:
        print(f)
        
def get_int(prompt):
    counter = 0
    while True and counter<=1:
        try:                                
            prompt = prompt.split("/")
            n, d = int(prompt[0]), int(prompt[1])
        
            f = round(100*(n / d))
            
            if f<0 or n>d:
                raise ValueError 
            elif f>= 99:
                return "F"
            elif f<=1:
                return "E"
            
            else:
                return (f"{f}%")                    
        except (ValueError, ZeroDivisionError):
            counter = counter + 1
            if counter <=1:
                prompt = input("Fraction: ") 
            pass

main()
        
        