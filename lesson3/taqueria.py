d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

ordered = []
def main():
    try:
        i = get_order(input("Item: "))      
        print(f"Total: {i:.2f}")        
    except EOFError:
        print()
        
    
def get_order(prompt):
    Total = 0
    while True:
        try:           
            o = prompt.title()
            if o not in d:
                raise KeyError
            Total = Total +d[o]
            ordered.append(o)
            print(f"Total: ${Total:.2f}")
            prompt = input("Item: ")  
        except  KeyError:
            prompt = input("Item: ")
            pass
        
            

main()