def main():
    
    greet = input("Greeting: ").strip()
    print(f"{value(greet)}")
    

def value(greeting):
    if greeting != "":
        first_char = greeting[0]
    else:
        x = 100
        return x

    if greeting.lower()[:5] == "hello":
        x = 0        
    elif first_char.lower() == "h" and greeting.lower()!="hello":
        x = 20        
    else:
        x = 100
    
    return x


if __name__ == "__main__" :
    main()