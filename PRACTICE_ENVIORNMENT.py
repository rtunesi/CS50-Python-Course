months = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

while True:
    try:
        date = input("Date: ").strip()  # Get user input and remove extra spaces

        # First, try parsing MM/DD/YYYY format
        if "/" in date:
            month, day, year = date.split("/")  # Split by "/"
            
            # Convert to integers to check validity
            month = int(month)
            day = int(day)
            year = int(year)
            
            # Ensure month and day are within valid range
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")  # Format YYYY-MM-DD
                break

        # Otherwise, try parsing "Month Day, Year" format
        elif "," in date:
            parts = date.split(" ")  # Split by space
            
            if len(parts) == 3:  # Ensure correct format
                month_name, day, year = parts[0], parts[1].strip(","), parts[2]
                
                if month_name in months:
                    month = months[month_name]  # Convert month name to number
                    day = int(day)
                    year = int(year)

                    # Ensure valid day range
                    if 1 <= day <= 31:
                        print(f"{year:04d}-{month}-{day:02d}")  # Format YYYY-MM-DD
                        break
    except ValueError:
        pass  # Ignore invalid inputs and ask again
