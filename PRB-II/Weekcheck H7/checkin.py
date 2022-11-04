import csv
import os, time
from datetime import datetime, timedelta

bookingFile = open('bookings_DX28.csv', 'r')
bookingList = list(csv.DictReader(bookingFile))
flight = bookingList[1]["flight_id"]
deadline = datetime.now() + timedelta(minutes=1)


def clear():
    os.system('cls')


def printWelcome():
    clear()
    print("\nWelcome to the check-in desk!")
    print(f"Check-in for flight: {flight}")
    print(f"Check-in closes at:  {deadline.strftime('%H:%M:%S')}")
    print(f"It is now:           {datetime.now().strftime('%H:%M:%S')}")
    input("\n\nPress enter to continue...")
    clear()


def booking():
    isRunning = True
    while isRunning:
        isFound = False
        num = input("Booking id: ")
        clear()

        for row in bookingList:
            if row['booking_id'] == num:
                isFound = True
                print(
                    f"{row['flight_id']}  |  {row['booking_id']}  |  {row['gender']}  |  {row['name']}")
                incheck = input("Do you want to check in? (Y/N)\n")
                clear()
                if incheck.lower() == 'y':
                    print("\nSuccesfully checked in.\n")
                    checkfile = open('checked_in.txt', 'w')
                    checkfile.write(f"{row['booking_id']}")
                    checkfile.close()
                else:
                    print("\nOk, not checked in.\n")
                print("----------------------------")
                exit = input("Press enter to continue or type 'X' to exit.\n")
                clear()
                if exit.lower() == 'x' or datetime.now() > deadline:
                    bookingFile.close()
                    isRunning = False
                    end_message()
        if isFound == False:
            print("Booking id not found.")


def end_message():
    print("Check-in closed. Goodbye\n")
    print("----------------------------")
    time.sleep(2)
    raise SystemExit


if __name__ == "__main__":
    printWelcome()
    booking()
