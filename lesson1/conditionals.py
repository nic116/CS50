'''
Conditionals

    syntax:
        >
        >=
        <
        <=
        ==
        !=
    
    if <_BOOLEAN EXPRESSION_>:
        'then' <__>
    boolean expression : has a true or false answer
'''

#Iteration 1: if, elif, else
'''
x = int(input("x = "))
y = int(input("y = "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
'''

# Iteration 2: or
'''
x = int(input("x = "))
y = int(input("y = "))
if x<y or x>y:
    print("x is not equeal to y")
else:
    print("x is equal to y")
'''

# Iteration 3: !=
'''
x = int(input("x = "))
y = int(input("y = "))
if x!=y:
    print("x is not equeal to y")
else:
    print("x is equal to y")
'''

#Iteration 4: and
'''
score = int(input("Score: "))
    # ways to ask
    #   score > a and score < b
    #   a <= score < b
    #   score >= a  Since we already know the values expected => improves program
if  90<= score <=100:
    print("Grade: A")
elif 80<= score <90:
    print("Grade: B")
elif 70<= score <80:
    print("Grade: C")
elif 60<= score<70:
    print("Grade: D")
else:
    print("Grade: F")
'''


# ITeration 5: % parity (remainder = modular arithmetics)
'''
x = int(input("x = "))
y = 2 #int(input("y = "))

if x % 2 ==0:
    print("Even")
else:
    print("Odd")
'''



# Iteration 5.1: using functions
'''
def main():
    x = int(input("x = "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2==0 else False

    if n % 2 ==0:
        return True
    else:
        return False
# The above is the same as:
*   return True if n % 2==0 else False
*   return n % 2 ==0
main()
'''

# Iteration 6: Mathc

name = input("What is your name? ")

if name == "" or "" or "":
    print("Gryffindor")
elif name == "":
    print("Slytherin")

match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")