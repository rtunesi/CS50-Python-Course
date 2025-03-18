grocery = {}

def main():
    while True:
        try:
            item = str(input()).upper()
            if item == "":
                break
            elif item in grocery:
                grocery[item] +=1
            else:
                grocery.update({item: 1})
        except EOFError:
            # Sort dictionary in alphabetical order
            for key in sorted(grocery.keys()):
                print(grocery[key], key)
            break


if __name__ == "__main__":
    main()

""" def main():
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
 """