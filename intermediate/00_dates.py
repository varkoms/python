### Dates ###

from datetime import datetime

now = datetime.now()
print(now) # 2023-03-02 15:16:26.545186

timestamp = now.timestamp()
print(timestamp) # 1677791969.979559

year_2023 = datetime(2023, 10, 12, 16, 50)
print(year_2023) # 2023-10-12 00:00:00

def print_date(date):
    # Time
    print(date.hour) 
    print(date.minute)
    print(date.second)

    # Dates
    print(date.day)
    print(date.month)
    print(date.year)

print_date(year_2023)