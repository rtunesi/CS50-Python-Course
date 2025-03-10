def main():
    fraction = fuel()
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")


def fuel():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            total = x / y
            if y == 0 or x > y:
                raise ValueError
            return round(total * 100)
        except (ValueError, ZeroDivisionError):
            pass

        

if __name__ == "__main__":
    main()