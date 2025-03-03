def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("How many times do you want to meow?: "))
        if n > 0:
            break
    return n 


def meow(n):
    for _ in range(n):
        print("meow")


main()

# V1.0
#def main():
#    n = int(input("How many times do you want to meow?: "))
#    meow(n)
#
#
#def meow(x):
#    for _ in range(x):
#        print("meow")
#
#
#main()