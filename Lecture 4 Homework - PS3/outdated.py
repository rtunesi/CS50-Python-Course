diary = [
    "Janruary",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ")
    try:
        # Splitting the date with /
        if "/" in date:
            month, day, year = date.split("/")
            print(month, day, year)
            if (int(month) >= 1 and int(month) <= 12):
                if (int(day) >= 1 and int(day) <= 31):
                    break
    except:
        pass

print(f"{year}-{month}-{day}")