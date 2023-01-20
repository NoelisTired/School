import pandas as pd
import os
import matplotlib.pyplot as plt


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
4a. Toon draaitabel van 4 gevolgd door een plot.
5. Toon plot van aantal passagiers per maand.
6. Sluit het programma.

""")

        clear()
        if option == "1":
            print(data['passengers'].mean())
            open('gemiddelde_passagiers.txt', 'w').write(
                str(data['passengers'].mean()))
        elif option == "2":
            top = int(input("Top: "))
            print((data.sort_values("passengers", ascending=False)).head(top))
            open('top_passagiers.txt', 'w').write(
                f"Top {top}: " + str((data.sort_values("passengers", ascending=False)).head(top)))
        elif option == "3":
            country = input("Land: ")
            print(data[data['destination'] == country]['destination'].count())
            open('vluchten_land.txt', 'w').write(f"Aantal vluchten naar {country}: " + str(
                data[data['destination'] == country]['destination'].count()))
        elif option == "4" or option.lower() == "4a":
            data['departed'] = pd.to_datetime(data['departed'])
            data['departed'] = data['departed'].dt.strftime('%Y/%m')
            table = data.pivot_table(
                index=data['departed'],
                columns='airline', 
                values='passengers', 
                aggfunc=sum)
            print(table)
            open('maandenVSairlines.txt', 'w').write(str(table))
            if option.lower() == "4a":
                table.plot(kind="barh", stacked=True)
                plt.show()
        elif option == "5":
            data['departed'] = pd.to_datetime(data['departed'])
            data['departed'] = data['departed'].dt.strftime('%Y/%m')
            plt.plot(data.groupby('departed')['passengers'].sum())
            plt.axis([data['departed'].min(), data['departed'].max(), data.groupby('departed')['passengers'].sum().min(), data.groupby('departed')['passengers'].sum().max()])
            plt.show()
        elif option == "6":
            break
        else:
            print("Invalid input")

    raise SystemExit


if __name__ == "__main__":
    main()
