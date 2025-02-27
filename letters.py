def main():
    guess_list = ["Jack", "Miran", "Callan", "Mat"]
    from_list = "Reece"
    for name in guess_list:
        print(letter(name, from_list))


def letter(recipient, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {recipient},
    
    You are invited to my sick birthday part located
    at Cool Skate park this evening at 7:00PM
    
    Sincerely,
    {sender}.
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


main()