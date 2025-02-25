def main():
    user_time = input("What time is it? ")
    if convert(user_time) >= 7.0 and convert(user_time) <= 8.0:
        print("breakfast time")
    elif convert(user_time) >= 12.0 and convert(user_time) <= 13.0:
        print("lunch time")
    elif convert(user_time) >= 18.0 and convert(user_time) <= 19.0:
        print("dinner time")
    else:
        print("Sorry I don't understand.")



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
