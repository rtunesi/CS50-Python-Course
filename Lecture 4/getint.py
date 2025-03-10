def main():
    x = get_int()
    print(f"The entered integer is: {x}")


def get_int():
    while True:
        try:
            x = int(input("Please enter your integer: "))
        except ValueError:
            # pass <- Use if you don't want to say anything and just catch the error.
            print("Please enter a valid integer.")
        else:
            return x 
    

if __name__ == "__main__":
    main()