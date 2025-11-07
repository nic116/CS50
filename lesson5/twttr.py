# Omit vowels (AEIOU) whether lower case or upper:


def main():
    tweet = input("Input: ")
    print(f"Output: {shorten(tweet)}")


def shorten(x):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    if x !="":
        for c in x:
            if c in vowels:
                x = x.replace( c, "")
        return x
    else:
        return x


if __name__ == "__main__":
    main()
