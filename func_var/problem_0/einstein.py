#prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer. 
# Assume that the user will input an integer.


def main():
    mass = int(input("m = "))
    energy(mass)


def energy(mass):
    c = 3 * int(pow(10,8))
    E = mass * int(pow(c,2))

    print(f"{E:,}")

main()
