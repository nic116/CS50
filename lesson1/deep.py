#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively)
# forty-two or forty two. Otherwise output No.


yes = ["42", "forty-two", "forty two"]

def main():
    quest = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer(quest)

def answer(n):
    if n.lower().strip() in yes:
        print("Yes")
    else:
        print("No")

main()
