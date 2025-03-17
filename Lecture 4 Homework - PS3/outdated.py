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
        # Splitting the date with , 
        elif "," in date:
            month, day, year = date.split(",")
