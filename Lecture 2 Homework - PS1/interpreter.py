user_input = input("Expression: ")
x, y, z = user_input.split(" ")
x = int(x)
z = int(z)

if y == "+":
    a = float(x + z)
    print(a)
elif y == "-":
    a = float(x - z)
    print(a)
elif y == "*":
    a = float(x * z)
    print(a)
elif y == "/":
    a = float(x / z)
    print(a)
else:
    print("Sorry I don't understand")