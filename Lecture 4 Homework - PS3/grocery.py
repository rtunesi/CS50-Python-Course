grocery = {}

def main():
    while True:
        item = str(input()).upper()

        try:
            if item == "":
                break
            elif not item in grocery:
                grocery.update({item: 1})
                print(grocery[item])
            else:
                grocery[item] += 1
                print(grocery[item])
        except EOFError:
            break

    print("Final Grocery List")
    for key, value in grocery.items():
        print(value, key)


if __name__ == "__main__":
    main()