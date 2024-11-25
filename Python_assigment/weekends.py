from datetime import datetime as dt

# List of dates in DD-MM-YYYY format
dates = ["18-11-2024", "19-11-2024", "20-11-2024", "21-11-2024", 
         "22-11-2024", "23-11-2024", "30-11-2024", "01-12-2024"]

# Filter weekends (Saturday and Sunday) with their day names
weekends = []
for date in dates:
    dt_obj = dt.strptime(date, "%d-%m-%Y")
    day = dt_obj.strftime("%A")
    if dt_obj.weekday() in (5, 6):
        weekends.append((date, day))

# Print weekends
for date, day in weekends:
    print(f"{date} is a {day}")
