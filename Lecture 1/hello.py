# Ask user to input their name.
name = input("What is your name? \n>: ")

# Remove whitespace from string.
name = name.strip()

# Capitalise first letter in string.
name = name.capitalize()

# Capitalise first letter in each word.
name = name.title()

# Combine the methods
name = name.strip().title()

# Say hello to the user.
print(f"Hello \"{name}\"")