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
            total = round(total)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    return total * 100
        

if __name__ == "__main__":
    main()