racers = ["Jack", "Mat"]

def main():
    global racers
    print("Welcome to the racers program.")
    print("Current listed racers:")
    printRacers()
    print("+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
    user_count = int(input("How many racers do you want to add?: "))
    for i in range(user_count):
        user_count -= 1
        new_racer = str(input("What is the racers name: "))
        addRacer(new_racer)
        print("New racer added successfully... ")
    print("\nThe racers have been amended, the current listed racers:")
    printRacers()


def addRacer(name):
    global racers
    racers.append(name)
    return racers


def printRacers():
    global racers
    for person in racers:
        print(person)


if __name__ == "__main__":
    main()