import csv
totalPassengers = 0
totalFlights = 0
with open("C:/Users/nmjjp/Documents/GitHub/School/PRB-II/WK6/arrivals.csv", "r", encoding="utf-8") as arrivals:
    reader = csv.DictReader(arrivals)
    for flight in list(reader):
        totalFlights += 1
        totalPassengers += int(flight["passengers"])
    print("Total passengers: " + str(totalPassengers))
    print("Total flights: " + str(totalFlights))