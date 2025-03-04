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

    # All vanity plate must start with at least two letters
    if carplate[0].isalpha() == False or carplate[1].isalpha() == False:
        return False

    # Numbers cannot be used in the middle of a plate: have to come at the end
    if carplate[2].isalpha() == False or carplate[3].isalpha() == False:
        return False

    # First number used cannot be a 0
    i = 0
    while i < len(carplate):
        if carplate[i].isalpha() == True:
            if carplate[i] == "0":
                return False
        else:
            break
        i += 1

    # No period, spaces or punctuation marks allowed
    for char in carplate:
        if char in forbidden:
            return False
        
    
    # If all tests are passed then return true
    return True


if __name__ == "__main__":
    main()