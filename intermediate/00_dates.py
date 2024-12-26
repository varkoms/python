### Dates ###
from datetime import date
from datetime import datetime
from datetime import time

# Prints every value given an specific date
def print_date(date):
    # Time
    print(date.hour)
    print(date.minute)
    print(date.second)

    # Dates
    print(date.day)
    print(date.month)
    print(date.year)


now = datetime.now()
print(now)  # Prints full date yyyy-mm-dd hh:mm:ss.xxxxxx

timestamp = now.timestamp()
print(timestamp)  # Print current timestamp

year_2024 = datetime(2024, 11, 22, 12, 41)
print(year_2024)  # Print specific date using year, month, date, hour and minute


# Call definition
print_date(year_2024)

# Create a new current_time
current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Modificando el año
print(current_date.year)

diff = year_2024 - now
print(diff)
