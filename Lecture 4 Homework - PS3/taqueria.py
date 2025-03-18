menu = {
    "BAJA TACO": 4.25,
    "BURRITO": 7.50,
    "BOWL": 8.50,
    "NACHOS": 11.00,
    "QUESADILLA": 8.50,
    "SUPER BURRITO": 8.50,
    "SUPER QUESADILLA": 9.50,
    "TACO": 3.00,
    "TORTILLA SALAD": 8.00
}

total = 0

while True:
    try:
        item = str(input("Item: ")).upper()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break

