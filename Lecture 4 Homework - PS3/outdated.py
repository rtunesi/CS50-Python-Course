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
            month = int(month)
            day = int(day)
            year = int(year)
            if (month >= 1 and month <= 12):
                if (day >= 1 and day <= 31):
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        # Splitting the date with ,
        elif "," in date:
            split = date.split(" ")
            if len(split) == 3:
                month_name, day, year = split[0].title(), split[1].strip(","), split[2]
                if month_name in diary:
                    month = diary[month_name]
                    month = int(month)
                    day = int(day)
                    year = int(year)
                    if (int(day) >= 1 and int(day) <=31):
                        print(f"{year:04d}-{month:02d}-{day:02d}")
                        break

    except:
        pass

