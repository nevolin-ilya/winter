
import datetime

def get_third_thursday(year, month):
    first_day_of_month = datetime.date(year, month, 1)
    first_thursday = first_day_of_month + datetime.timedelta(days=(3-first_day_of_month.weekday() + 7)%7)
    third_thursday = first_thursday + datetime.timedelta(weeks=2)
    return third_thursday

year = 2024

for month in range(1, 13):
    third_thursday = get_third_thursday(year, month)
    print(third_thursday)

