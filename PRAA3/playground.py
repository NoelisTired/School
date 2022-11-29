import datetime
from datetime import date

def calculate_age(born):
    today = date.today()
    print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

print(calculate_age(datetime.date(1949, 6, 24)))