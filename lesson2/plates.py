# Check the valdity of the number plates:
#   first 2 elements are letters
#   maximum 6 characters, minimum 2 characters
#   numbers at the end (not in the middle)
#   first number cannot be 0
#   no periods, spaces or punctuation allowed.

import string

def main():
    plate = input("Plate: ")
    result = is_valid(plate)
    is_valid(plate)
    #print(result)
    if result[0]==False:
        #print(result)
        print("Invalid")
    else:
        #print(result)
        print("Valid")


def is_valid(s):
    l = list(s)
    if 2<= len(l) <= 6:
        l_num = []
        for char in l[:2]:
            if char.isalpha() != True:
                validity = False
                return validity, "alpha fail"
           
        for char in l[2:-1]:
            if char in string.punctuation or char == " ":
                validity = False
                return validity, "punct fail"
            if char.isnumeric()==True:
                l_num.append(char)

        if l[-1].isnumeric()==False or l_num[0] == '0':
            validity = False
            return validity, "numb fail"
        else:
            validity = True
            return validity, "pass"
        

main()

#        for i in range(0, len(l)):
#            if l[0].isnumeric() != False or l[1].isnumeric() != False:
#                return False
#            elif l[i] in string.punctuation:
#                return False
            

# txt.isnumeric()
# txt.isalpha()
# if char in string.punctuation:
#   print(f"{char}")


