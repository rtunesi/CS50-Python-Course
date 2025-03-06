vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

user_input = str(input("Input: "))

print("Output: ", end="")

for char in user_input:
    if char not in vowel:
        print(char, end="")