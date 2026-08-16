def main():

    difficulty = input("what's the difficulty level? ")

    if not  difficulty == "Difficult" or difficulty == "Easy":
            print ("Invalid input")
            return

    players = input("Multiplayer or Single-player? ")

    if not players == "Multiplayer" or players == "single-player":
            print ("Invalid input")
            return

    if difficulty == "Difficult" and players == "Multiplayer":

            recommend(" Stand off 2")

    elif difficulty == "Difficult" and players == "single-player":

            recommend(" Cuphead")

    elif difficulty == "Easy" and players == "Multiplayer":

            recommend("Free Fire")

    else:

            recommend(" Subway surfers")


def recommend(game):
    print(f"you might like {game}")

main()




