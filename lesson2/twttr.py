# Omit vowels (AEIOU) whether lower case or upper:

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

def main():
    tweet = input("Input: ")
    vowel_remover(tweet)


def vowel_remover(x):
    for c in x:
        if c in vowels:
            x = x.replace( c, "")
    print("Output:", x)


main()
