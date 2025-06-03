'''
Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
'''

x = input("Say something: ")
def playback():
    y = x.split(' ')
    y_str = [str(i) for i in y]
    y_join = "...".join(y_str)
    print(y_join)
    return

playback()
