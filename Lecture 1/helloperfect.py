# Main part of the program - def as main
def main():
    name = input("What is your name? \n>: ").strip().title()
    hello(name)                             # This calls (1.)

# Hello function - prints persons name
def hello(to="Person"):                     # (1.) Main function calls this
    print(f"Hello {to}")

# Start the program
main()