import inflect

p = inflect.engine()


def main():

    name_list = []

    while True:
        try:
            name = input("Name: ")
            if name == "":
                raise ValueError
            else:
                name_list = name_list + [name.title()]
        
        except ValueError:
            name =  input("Name: ")
            pass
        except EOFError:
            break
    names = p.join(name_list, final_sep="")
    print(f"\nAdieu, adieu, to {names} " )

main()