


def main():
    try:
        l = get_list(input())
        print()
        for k in l:
            print(f"{l[k]}", f"{k}")
    except EOFError:
        pass

def get_list(prompt):
    d = {}
    o = 0
    item = prompt.upper() 
    while True:
        
        try:               
            if item in d:
                o = d[item] + 1
                d.update({item : o })
            else:                   
                d.update({item:1})
                
            item = input().upper()
        
        except EOFError:
            break

    sorted_item = {k : v for k,v in sorted(d.items())}
    return sorted_item
main()