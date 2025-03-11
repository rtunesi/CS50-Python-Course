grocery = {}
while True:
    item = str(input())

    if not item in grocery:
        grocery.update({item: 1})
        print(grocery[item])
    else:
        grocery[item] += 1
        print(grocery[item])