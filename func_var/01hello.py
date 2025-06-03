#############
# Lesson 1: STR
#############

# Iteration 1
' print("Hello, world") '

# Iteration 2 

' name = input("What is your name? ") '

# + adds the second value to the previous straight after.
' print("Hello, " + name) '

# , adds a space in between the two values.
' print("Hello," , name) '

#    comments: <#>, <""""">
# use of pseudocode as a small checklist/flowchart
# helps for creating a to-do list



#Iteration 3 - print Function

#doc for pring t function

#    print(*objects, sep='', end= '\n' , files=sys.st)dout, flush=False)
#        \n : end every line by starting a new line.
#        sep: separate values by a space " ".

name = input("What is your name? ")
' print("Hello," , end="") '
' print(name) '

' print("Hello," , name, sep="???") '

# Note: use \"...\" to print quotes

#Iteration 4: format string
' print(f"Hello, {name}") '


#Iteration 5: str formating
# eg: bad input, that we can clean up.

#   Remove whitespace from str:
' name = name.strip() '

#   Capitalise the FIRST letter
' name = name.capitalize() '

# Capitalise the First Letter of EVERY letter
' name = name.title() '

# Capitalise and remove whitespace
' name = input("What is your name?").title().strip() '

# Split string. E.g.: first name and last name
' first, last = name.split(" ") '

' print(f"hello, {first} {last}") '



