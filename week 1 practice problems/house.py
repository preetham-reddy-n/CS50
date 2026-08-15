name = input("What's your name? ")

match name:
    case "Harry" | "Hemione" | "Ron":
        print("Griffyndor")


    case "Draco":
        print("Slytherin")

    case _:
        print("Who?")
