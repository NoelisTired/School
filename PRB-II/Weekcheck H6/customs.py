import csv
animalsFile = open("animals.csv", "r")
reader = csv.DictReader(animalsFile)
animalsList = list(reader)
totalValue = 0
totalCountry = 0.0

country = input("Enter a country:\n")

for animal in animalsList:
    print(f"{animal['animal']}")
    totalValue += float(animal['import_value'])
    if animal['country_of_origin'] == country.capitalize():
        totalCountry += 1

print("--------------------")
print(f"Total value: {totalValue}")
print(f"Average value: {totalValue/len(animalsList)}")
print(f"Total animals for '{country.capitalize()}': {int(totalCountry)}")