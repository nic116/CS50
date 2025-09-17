'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''



cash_in = []


def main():
    print("Amount Due: 50")
    x = int(input("Insert Amount: "))

    while x not in [5, 10, 25]:
        main()
    else:
        cash_in.append(x)
        change(x)


def change(n):
    while True:
        cash_total = sum(cash_in)
        if 50 - cash_total > 0:
            print("Amount Due:", int(50-cash_total))
            n = int(input("Insert Coin: "))
            if n in [5, 10, 25]:
                cash_in.append(n)
            else:
                pass
        else:
            if 50 - cash_total == 0:
                print("Change Owed:", 50 - cash_total)
                return False
            else:
                print("Change Owed:", cash_total - 50)
                return False


main()

