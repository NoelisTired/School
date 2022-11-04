import csv
import os
from datetime import datetime, timedelta

maintFile = open('maintenance.csv', 'r')
maintList = list(csv.DictReader(maintFile))

def clear():
    os.system('cls')

while True:
    option = input("""
Please select an option:
1. Show planes that need maintenance in the coming [x] months.
2. Show [y] amount of planes that had maintenance lately. 
3. To exit.

Choice: """)
    if option == '1':
        clear()
        months = int(input("How many months in advance do you want to check? "))
        today = datetime.now()
        check_date = today + timedelta(days=months*30)
        clear()

        for row in maintList:
            end = datetime.strptime(row['checkup_before'], "%d/%m/%Y")
            if end < check_date and end > today:
                print(f"{row['plane_id']}  |  {row['checkup_before']}")
    
    elif option == '2':
        clear()
        amount = int(input("How many planes do you want to check? "))
        clear()
        data_sorted = sorted(maintList, key=lambda plane:datetime.strptime(plane['last_checkup'], "%d/%m/%Y"), reverse=True)
        breaktime = 0

        for row in data_sorted:
            if breaktime == amount:
                break
            else:
                print(f"{row['plane_id']}  |  {row['last_checkup']}")
                breaktime += 1

    elif option == '3':
        maintFile.close()
        break
