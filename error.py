while True:
    try:
        x = int(input("What is x?: "))
    except ValueError:
        print("x is not an integer, try again.")
        print()
    else:
        break

print(f"x = {x}")