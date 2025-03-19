diary = {
    "Janruary": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    date = input("Date: ")
    try:
        # Splitting the date with /
        if "/" in date:
            month, day, year = date.split("/")
            if (int(month) >= 1 and int(month) <= 12):
                if (int(day) >= 1 and int(day) <= 31):
                    print(f"{year}-{month}-{day}")
                    break
        # Splitting the date with ,
        elif "," in date:
            split = date.split(" ")
            if len(split) == 3:
                month_name, day, year = split[0].title(), split[1].strip(","), split[2]
                if month_name in diary:
                    month = diary[month_name]
                    if (int(month) >= 1 and int(month) <=12):
                        if (int(day) >= 1 and int(day) <=31):
                            if month <= 9 and int(day) <= 9:
                                print(f"{year}-0{month}-0{day}")
                            elif int(day) <= 9:
                                print(f"{year}-{month}-0{day}")
                            elif month <= 9:
                                print(f"{year}-0{month}-{day}")
                            else:
                                print(f"{year}-{month}-{day}")
                        break

    except ValueError:
        pass

