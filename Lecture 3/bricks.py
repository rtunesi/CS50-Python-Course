for i in range(3):
    print("#")

print("----------")

def main():
    amount = int(input("How many bricks do you want printed?: "))
    printBricks(amount)

def printBricks(n):
    for _ in range(n):
        print("#")

main()