groceries = []
choice = 0

while choice != 4:
    print("[1] Add Item")
    print("[2] View Item")
    print("[3] Remove Item")
    print("[4] Exit")
    choice = int(input("Choose a feature: "))

    match choice:
        case 1: 
            add = input("place an item in the basket: ")
            groceries.append(add)
            print(f"{add} is added on to the basket.")
        case 2:
            if len(groceries) > 0: 
                for item in groceries:
                    print(item)
            else: print("There is nothing in basket.")
        case 3:
            try:
                min = input("Remove an item: ")
                groceries.remove(min)
                print(f"{min} is removed from basket.")
            except:
                print("Not in list.")
        case 4:
            print("Goodbye!")
            break

"""
well done! you should add error handling when the user accidentally inputs the wrong datatype though! :D
"""
