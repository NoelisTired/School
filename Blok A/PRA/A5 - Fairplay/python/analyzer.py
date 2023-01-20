import pandas as pd
from datetime import datetime, timedelta
import lib_bamboo as bamboo
import os, math

if os.name == "nt":
    os.system('cls')
else:
    os.system('clear')
print(f"{'[-] Working' : >360}")

data = pd.read_excel("python/Volleybal_Eredivisie_tussenstand.xlsx")
data["datum"] = pd.to_datetime(data["datum"], format="%d/%m/%Y")
data = data.sort_values("datum")

#Informatievraag 1
totalFaults = data['overtredingen'].sum()
file1 = open("files/totalovertredingen.txt", "w", 
            encoding="UTF-8")
file1.write(
    str(totalFaults)
)
file1.close()
print(f"{'[+] Successfully exported totalovertredingen.txt | 1/6' : >350}", end=f" : 16.66%\n")

#Informatievraag 2
averageFaults = data["overtredingen"].mean()
file2 = open("files/average.txt", "w", 
            encoding="UTF-8")
file2.write(
    str(
        round(
            float(averageFaults)
        )
    )
)
file2.close()
print(f"{'[+] Successfully exported average.txt | 2/6' : >350}", end=f" : 33.33%\n")

#Informatievraag 3
zwartBoek = data.sort_values("overtredingen",
                                ascending=False).head(5)
file3 = open("files/zwartboek.txt", "w", 
            encoding="UTF-8")
file3.write(
    bamboo.prettify(zwartBoek, 
                    type="zwartboek")
)
file3.close()
print(f"{'[+] Successfully exported zwartboek.txt | 3/6' : >350}", end=f" : 50.00%\n")

#Informatievraag 4
file4 = open("files/eregalerij.txt", "w",
            encoding="UTF-8")
file4.write(
    bamboo.prettify(
        data[(data["overtredingen"] < 2) & (data["datum"] >= datetime.now() - pd.Timedelta(days=21))],
        type="eregalerij")
)
file4.close()
print(f"{'[+] Successfully exported eregalerij.txt | 4/6' : >350}", end=f" : 66.66%\n")

"""
    Voor de Excellente Beoordeling:
    De volgende 2 vragen zijn wat lastiger, omdat je hier een pivot table moet maken.   
"""
#Informatievraag 5
data["month"] = data["datum"].dt.month
table = data.pivot_table(values='overtredingen',
                        index='scheidsrechter',
                        columns='month',
                        aggfunc='sum')
file5 = open("files/scheidsrechters.txt", "w", 
            encoding="UTF-8")
file5.write(
    bamboo.prettify(table)
)
file5.close()
print(f"{'[+] Successfully exported scheidsrechters.txt | 5/6' : >350}", end=f" : 83.33%\n")

#Informatievraag 6
data["month"] = data["datum"].dt.month
table = data.pivot_table(values='bezoekersaantal',
                        index='stadion',
                        columns='month',
                        aggfunc='sum')
file6 = open("files/stadion_bezoekers.txt", "w",
            encoding="UTF-8")
file6.write(
    bamboo.prettify(table)
)
file6.close()
print(f"{'[+] Successfully exported stadion_bezoekers.txt | 6/6' : >350}", end=f" : 100.00%\n")
table.to_csv('files/stadion_bezoekers.csv') #! Export naar CSV
print("CSV Exported")
print("Done!")
