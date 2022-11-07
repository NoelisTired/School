import csv
arrivalsFile = open("arrivals.csv", "r")
reader = csv.DictReader(arrivalsFile)
arrivalsList = list(reader)

for arrival in arrivalsList:
    print(f"At {arrival['arrival']} a {arrival['airline']} flight from the city of {arrival['origin']} has landed, carrying {arrival['passengers']} passengers.\n")
