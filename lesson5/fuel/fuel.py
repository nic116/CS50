

def main():
    while True:
        fraction = input("Fraction: ")
        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError): 
            continue

def convert(prompt):
   try:        
        prompt = prompt.split("/")
        n, d = int(prompt[0]), int(prompt[1])
        if d == 0:
            raise ZeroDivisionError
        if n>d or n<0 or d<0:
            raise ValueError
        percent = round(100*(n/d))
        return percent
   except (ValueError, AttributeError):
       raise ValueError
     
def gauge(f):
    
    if f <=1:
        return "E"
    elif f >=99:
        return "F"
    else:
        return f"{f}%"

if __name__ == "__main__":
    main()        