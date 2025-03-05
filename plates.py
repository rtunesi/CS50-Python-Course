def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(carplate):
    forbidden = [".", " ", "!", "?", ","]
    # vanity plates may contain a maxium of 6 characters
    # and a minimum of 2 characters
    if len(carplate) < 2 or len(carplate) > 6:
        return False

    # check the plate starts with at least two letters
    # is.alpha() returns True is the compaired value is a letter
    if not(carplate[:2].isalpha()):
        return False
    
    # check there isn't any punctuation
    for char in carplate:
        if char in forbidden:
            return False
        
    # check placement rules
    has_number = False  # Track if we've seen a number
    for i, char in enumerate(carplate):
        if char.isdigit():  # If it's a number
            if not has_number:  # First time seeing a number
                if char == "0":  # First number cannot be 0
                    return False
                has_number = True  # Mark that we've seen a number
        elif has_number:  # If we see a letter AFTER a number, it's invalid
            return False


    return True
 


if __name__ == "__main__":
    main()