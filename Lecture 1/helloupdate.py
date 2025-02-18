def hello(to="person"):
    print(f"Hello {to}")

hello()
name = input("What's your name? \n>: ").strip().title()
hello(name)
