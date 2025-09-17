'''
Content:
    Dictionaries
    Dictionary methods
    For loops
    Lists
    Lists and Dictionary Comprehensions
    List Methods
    String Slicing
    Tuples
    While Loops
'''

# Iteration 1: while
'''
i = 3
while i !=0:
    print("meow")
    i = i -1
'''

# Iteration 2: for
'''  
for i in [0,1,2]:   #for will loop through the elements in the list
    print("meow")

for _ in range(3):  #for will loop through the elements in the range
    print("meow")   # pythonic convention use _ for a variable that is only used to cycle through in a single function

print("meow\n"*3, end="")   #\n will move to new line. Use end="" to not do the last \n.
'''

# to automatically check if a condition is satisfied
'''
while True:
    n = int(input("What is n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")
'''
# As a function
'''
def main():
    numeber = get_number()
    meow(numeber)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n>0:
            return n
    #return n

def meow(n):
    for _ in range(n):
        print("meow")
main()
'''

# Iteration 3: Lists "list" = ["value"]
'''
students = ["Hermione", "Harry", "Ron"]

for student in students:    # student variable is defined by us, (= x in students)
    print(student)
# simmilarlly 
for i in range(len(students)):   
    print(i + 1, students[i])
'''


# Iteration 4: Dictionaries "dict"  = {"key": "Value"}
'''
students = {"Hermione":"Gryffindor", 
            "Harry":"Gryffindor", 
            "Ron":"Gryffindor", 
            "Draco":"Slytherin"
            }
print(students["Hermione"])
for student in students: #for loop over dictionaries only print out keys
    print(student, students[student], sep=", ")
'''
# dictionary with multiple values:
students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus": None} #None is a nil value
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

## Iteration 5: practical case mario blocks
'''
for _ in range(3):
    print("#")

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
'''
## Iteration 5.1: row of blocks
def main():
    print_row(4)

def print_row(width):
    print("?" * width)
main()

# Iteration 5.2: 2D of blocks
def main():
    print_square(3)

def print_square(size):
    #for each row in squeare
    for i in range(size):
        #for each brick in row.     Can also have print("#" * size)
        for j in range(size):
            # print brick
            print("#", end="")
        #prints a new line similar to \n
        print()