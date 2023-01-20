#Gerechten: basislijsten
gerechtenMaandag = ["Forel", "Kreeft", "Zalm", "Vissticks", "Kogelvis"]
gerechtenDinsdag = ["Falafel", "Vega lasagne", "Geitenkaassalade", "Friet", "Stoofpotje kikkererwten"]
gerechtenWoensdag = ["Friet", "Broodje kroket", "Kaassouflé", "Frikandel", "Bamihap"]
gerechtenDonderdag = ["Lorem", "Ipsum", "Dolor", "Sit", "Amet"]

#Gerechten: combilijsten
gerechtenVrijdag = gerechtenMaandag + gerechtenDonderdag
gerechtenWeekend = gerechtenMaandag + gerechtenDinsdag + gerechtenWoensdag + gerechtenDonderdag

#Dranken
dranken = ["Bier", "Cola", "Wijn", "Sinas", "Koffie", "Thee", "Sterke drank"]

isRunning = True
while isRunning:
  #Inputs
  print("Welkom bij HBG Horeca. Voer een Q in om af te sluiten.\n")
  dag = input("Welke dag is het vandaag (kleine letters)? ")
  if dag.upper() == "Q":
    break

  gerechtVanDeDag = input("Wat is het gerecht van de dag? ")
  if gerechtVanDeDag.upper() == "Q":
    break

  print("\n")

  if dag == "maandag":
    gerechtenVandaag = gerechtenMaandag
  elif dag == "dinsdag":
    gerechtenVandaag = gerechtenDinsdag
  elif dag == "woensdag":
    gerechtenVandaag = gerechtenWoensdag
  elif dag == "donderdag":
    gerechtenVandaag = gerechtenDonderdag
  elif dag == "vrijdag":
    gerechtenVandaag = gerechtenVrijdag
  elif dag == "zaterdag" or dag == "zondag":
    gerechtenVandaag = gerechtenWeekend

  #Loop
  for gerecht in gerechtenVandaag:
    if gerecht == gerechtVanDeDag:
      print(f"Gerecht van de dag: {gerecht}")
    else:
      print(gerecht)

  print("\n")

  for drank in dranken:
    if drank == "Sterke drank":
      if dag == "zaterdag" or dag == "zondag":
        print(drank)
    else:
      print(drank)

  print("\n")