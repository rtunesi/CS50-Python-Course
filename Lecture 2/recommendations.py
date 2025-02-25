def main():
    difficulty = input("Diifcult or Casual?: ").lower()
    players = input("Singleplayer or Multiplayer?: ").lower()

    if difficulty == "difficult":
        if players == "singleplayer":
            recommend("Solitaire")
        else:
            recommend("Bullshit")
    else:
        if players == "singleplayer":
            recommend("Pyramid")
        else:
            recommend("21")


def recommend(game):
    print(f"You might like: {game}")


main()