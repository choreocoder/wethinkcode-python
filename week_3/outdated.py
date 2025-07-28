months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    user_date = input("Enter Date: ").strip()

    try:
        # Handle MM/DD/YYYY format
        if "/" in user_date:
            parts = user_date.split("/")
            if len(parts) != 3:
                continue
            month, day, year = map(int, parts)

        # Handle MonthName DD, YYYY format - must have comma
        elif any(user_date.startswith(month) for month in months):
            if "," not in user_date:
                continue  # reject if comma is missing
            user_date = user_date.replace(",", "")
            parts = user_date.split()
            if len(parts) != 3:
                continue
            month_name, day, year = parts
            if month_name not in months:
                continue
            day = int(day)
            year = int(year)
            month = months.index(month_name) + 1

        else:
            continue

        # Validate date ranges
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        continue
