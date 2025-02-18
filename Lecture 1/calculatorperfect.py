# Main part of the program - def as main
def main():
    x = int(input("What is x? \n>: "))
    print(f"x squared is: {square(x)}")     # This calls the square funcion to run (1.)

# Square function - squares the number
def square(n):                              # (1.) Line 4 calls this function.
    return n * n

main()