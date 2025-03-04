# Get user input
user_camel = str(input("camelCase: "))

# Print "snake_case: "
print("snake_case: ", end="")

# Loop through every letter
for char in user_camel:

    # Check if letter is upper case
    if char.isupper():

        # Print underscores and the letter in lowercase
        print(f"_{char.lower()}", end="")

    # Otherwise print letter
    else:
        print(char, end="")
