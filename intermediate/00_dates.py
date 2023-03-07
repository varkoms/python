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

from datetime import time

current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Modificando el año
print(current_date.year)