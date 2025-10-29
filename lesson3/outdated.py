


# Using 2 def: one if the input are numeric, one if the is alphabetic

def main():
    
    date = input("Date: ")
    date_num = date.replace(" ", "")                    #needed to remove empty space " 9/8/1636 " (just for this case)
    
    if date_num[0].isnumeric() == True:
        d = num_date(date_num)
        print(d)

    elif date[0].isalpha() == True:
        try:
            if date[-6] != ",":                         #picking bad formating (no ',') before reaching function
                raise ValueError
            else:
                d = alph_date(date)
                print(d)
        except ValueError:
            main()
            pass


def num_date(prompt):
    
    try:
        prompt = prompt.replace(" ", "")                #removes empty spaces
        prompt = prompt.split("/")                      #split the string into list
        for i in range(0,len(prompt)):
            prompt[i] = "%02d" % (int(prompt[i]),)      #makes 2 digit number every element
        
        prompt = {                                      #ordered dictionary to return
            "YYYY": prompt[2],
            "MM": prompt[0],
            "DD": prompt[1]
        }
        if int(prompt["DD"])< 1 or 31 < int(prompt["DD"]):
            raise ValueError                            # value error raised if value not acccepted for 
        elif int(prompt["MM"])> 12:
            raise ValueError
            
        else:
            date = "-".join(prompt.values())            #joins values to string
            return date                                 #returns the string in format YYYY-MM-DD
    except ValueError:
        main()
               
        pass
        


def alph_date(alph_prompt):
    
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July":"07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November" : "11",
        "December": "12"
        }
    
    try:
        
        alph_prompt = alph_prompt.replace(",", "").split(" ")
        if alph_prompt[0] in months and int(alph_prompt[1])< 32:        #check for month in dic and DD in range
            date = {
                            "YYYY": alph_prompt[2], 
                            "MM": months[alph_prompt[0]], 
                            "DD": "%02d" % (int(alph_prompt[1]),)
                            }
            date = "-".join(date.values())
            return date
        
        else:
            raise ValueError
    except ValueError:
        main()
        pass

    


    
if __name__ == "__main__":
    main()
