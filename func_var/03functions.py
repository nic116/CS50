
# defining a parameter
# Iteration 1
'''
def hello(to):
    #parameter will will be stored in the function as to.
    print("hello,", to)


name = input("What is your name? ")
hello(name)
'''

# Iteration 2:
'''
def hello(to = "world"):
    #parameter will will be stored in the function as to.
    print("hello,", to)

#prints with locally stored value
hello()
name = input("What is your name? ")
#prints outside value
hello(name)
'''

# Iteration 3:
# create a main function to

'''
def main():
    name= input("What is your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
'''

#return

def main():
    x = int(input("What is x? ")) 
    print("x square is ", square(x))

def square(n):
    return pow(n, 3)
    # also: n*n or n**3 or pow(n, 3)

main()