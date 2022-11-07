import pandas as pd
import os
from datetime import datetime
from datetime import timedelta

data = pd.read_csv("bagage.csv")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    option = input("""Toon mij...
1. Gemiddelde gewicht van alle vervoerde bagage
2. Totale gewicht voor vlucht met nummer [X]
3. Gemiddelde gewicht van alle stukken ervoerd door maatschappij [X] met bestemming [Y]
4. Aantal stukken voor bestemming [X] met een incident
5. Aantal stukken van maatschappij [X] met een incident, die zijn ingeladen door medewerker [Y]
6. Aantal dieren waarbij een incident plaatsvond, geteld voor maatschappij [X]
7. Aantal dieren waarbij een incident plaatsvond, geteld voor medewerker [X]
8. Gemiddeld aantal overstappen voor breekbare stukken, vervoerd door maatschappij [X]
9. Aantal breekbare stukken met een incident dat door maatschappij [X] is vervoerd in ruim [Y]
10. Aantal incidenten in de 30 dagen vanaf datum [X]
11. Top 20 bagagestukken met het hoogste gewicht
X. Exit

Option: """)
    if option.lower() == 'x':
        exit()
    elif option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "5":
        option5()
    elif option == "6":
        option6()
    elif option == "7":
        option7()
    elif option == "8":
        option8()
    elif option == "9":
        option9()
    elif option == "10":
        option10()
    elif option == "11":
        option11()
    else:
        main()

def option1():
    clear()
    print("Gemiddelde gewicht:",data["gewicht"].mean())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option2():
    clear()
    flight = input("Vlucht: ")
    clear()
    print(f"Totale gewicht voor vlucht {flight}:",(data[data["vlucht"] == flight]["gewicht"].sum()).round(2))
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option3():
    clear()
    company = input("Maatschappij: ")
    destination = input("Bestemming: ")
    clear()
    print(f"Gemiddelde gewicht van alle stukken ervoerd door maatschappij {company} met bestemming {destination}:",data[(data["maatschappij"] == company) & (data["bestemming"] == destination)]["gewicht"].mean())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option4():
    clear()
    destination = input("Bestemming: ")
    clear()
    print(f"Aantal incidenten in richting Germany:",data[(data["bestemming"] == destination) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option5():
    clear()
    company = input("Maatschappij: ")
    employee = input("Medewerker: ")
    clear()
    print(f"Aantal incidenten voor {company} met medewerker {employee}:",data[(data["maatschappij"] == company) & (data["ingeladen_door"] == employee) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main() 

def option6():
    clear()
    company = input("Maatschappij: ")
    clear()
    print(f"Aantal incidenten met een dier voor {company}:",data[(data["maatschappij"] == company) & (data["dieren"] != 0) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option7():
    clear()
    employee = input("Medewerker: ")
    clear()
    print(f"Aantal incidenten met een dier voor {employee}:",data[(data["ingeladen_door"] == employee) & (data["dieren"] != 0) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option8():
    clear()
    company = input("Maatschappij: ")
    clear()
    print(f"Gemiddeld aantal overstappen voor breekbare stukken, vervoerd door maatschappij {company}:",data[(data["maatschappij"] == company) & (data["breekbaar"] != 0)]["aantal_overstappen"].mean())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option9():
    clear()
    company = input("Maatschappij: ")
    room = input("Ruim: ")
    clear()
    print(f"Aantal incidenten voor breekbare items vervoerd door maatschappij {company} in ruim {room}:",data[(data["maatschappij"] == company) & (data["vrachtruim"] == room) & (data["breekbaar"] != 0) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option10():
    clear()
    date = input("Datum (dd-mm-yyyy): ")
    date = datetime.strptime(date, "%d-%m-%Y")
    date_end = date + timedelta(days=30)
    data["vertrekdatum"] = pd.to_datetime(data["vertrekdatum"])
    clear()
    print(f"Aantal incidenten in de 30 dagen tusesn datum {date} en datum {date_end}:",data[(data["vertrekdatum"] > date) & (data["vertrekdatum"] < date_end) & (data["incidenten"] != "")]["incidenten"].count())
    exit = input("Press enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def option11():
    clear()
    indexNumber = 0
    top20 = data.sort_values("gewicht", ascending=False).head(20)
    clear()
    for weight in top20["gewicht"]:
        indexNumber += 1
        print(f"{indexNumber}. {weight}kg op vlucht {top20.iloc[indexNumber-1]['vlucht']} richting {top20.iloc[indexNumber-1]['bestemming']}")
    exit = input("\nPress enter to continue or 'X' to exit... ")
    if exit.lower() == "x":
        exit()
    else:
        main()

def exit():
    clear()
    raise SystemExit

if __name__ == "__main__":
    main()