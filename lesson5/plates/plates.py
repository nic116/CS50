def main():
    plate = input("Plate: ")
    if is_valid(plate)==True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    p = list(s)
       
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(p)<2 or 6<len(p):
        return False

    #“All vanity plates must start with at least two letters.”
    if str(p[0]).isalpha() == False or str(p[1]).isalpha() == False:    
        return False
    
        
    
    #“Numbers cannot be used in the middle of a plate; they must come at the end. 
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
    # The first number used cannot be a ‘0’.”
     
    r = []      #empty list to separate the begining of what is not a letter


    for i in range(2, len(p)):              # loop from i=2 since we already know previous
        if str(p[i]).isalpha() == False:
            r = r + p[i:]                   #append everything from failure point
            if str(r[0]) == "0":
                return False
            break                           # because we dont need to keep iterating
            

    #“No periods, spaces, or punctuation marks are allowed.”
    for j in r:
        if str(j).isnumeric() == False:
            return False                    # return false if anything other than number (e.g. punctuation, letter)
    
    return True                             # natural value if nothing fails


if __name__ == "__main__":
    main()