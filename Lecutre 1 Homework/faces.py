def convert(str):
    str = str.replace(str.replace(":)", "🙂").replace(":(", "🙁"))
    return str

def main():
    user_input = input(">: ")
    print(convert(user_input))

main()