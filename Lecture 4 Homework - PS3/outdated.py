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
            day, month, year = date.split("/")
            print(day, month, year)
        # Splitting the date with , 
        elif "," in date:
            day, month, year = date.split(",")
