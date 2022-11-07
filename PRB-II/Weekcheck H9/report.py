import pandas as pd
import os

def clear():
    os.system('cls')


def main():
    clear()
    while True:
        data = pd.read_excel("flights_2019.xlsx")

        option = input("""
1. Toon gemiddelde aantal passagiers
2. Toon de top [Z] van vluchten met meeste passagiers
3. Toon aantal vluchten naar [Land]
4. Toon draaitabel van maanden vs airlines, met som van passagiers
5. Sluit het programma.

""")

        clear()
        if option == "1":
            print(data['passengers'].mean())
            open('gemiddelde_passagiers.txt', 'w').write(str(data['passengers'].mean()))
        elif option == "2":
            top = int(input("Top: "))
            print((data.sort_values("passengers", ascending=False)).head(top))
            open('top_passagiers.txt', 'w').write(f"Top {top}: " + str((data.sort_values("passengers", ascending=False)).head(top)))
        elif option == "3":
            country = input("Land: ")
            print(data[data['destination'] == country]['destination'].count())
            open('vluchten_land.txt', 'w').write(f"Aantal vluchten naar {country}: " + str(data[data['destination'] == country]['destination'].count()))
        elif option == "4":
            table = data.pivot_table(
                index='departed',
                columns='airline', 
                values='passengers', 
                aggfunc=sum)
            print(table)
            open('maandenVSairlines.txt', 'w').write(str(table))
        elif option == "5":
            break
        else:
            print("Invalid input")
    
    raise SystemExit
    
if __name__ == "__main__":
    main()