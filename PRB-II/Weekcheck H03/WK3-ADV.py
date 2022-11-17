import os, time
from data import planeLandedList, hangarList
toPark = []
while True:
    if os.name == 'nt': #? Windows
        os.system('cls')
    else:
        os.system('clear') #? Linux
    
    print("Welkom bij HangarParkeerder3000")
    print("-"*30)
    print("Deze vliegtuigen wachten om geparkeerd te worden")
    for plane in planeLandedList:
        if plane['hangar'] == 0:
            toPark.append(plane)
            print("%s (type: %s)" % (plane['code'], plane['type']))
    planeInput = input("\nVoer code in: ")
    print("\nDeze hangars zijn nog vrij: ")
    for hangar in hangarList:
        if not hangar['occupied']:
            print("Hangar %s is nog vrij" % hangar['num'])
    hangarInput = input("In welke hangar wil je het vliegtuig parkeren: ")
    for plane in planeLandedList:
      if plane['code'] == planeInput:
        for hangar in hangarList:
          if hangar['num'] == int(hangarInput):
            if hangar['occupied']:
              print("Hangar %s is al bezet" % hangar['num'])
              time.sleep(2)
            else:
              print("Beep-Beep, Je hebt %s geparkeerd in Hangar %s" % (planeInput, hangar['num']))
              plane['hangar'] = hangar['num']
              hangar['occupied'] = True
              time.sleep(2)
    print("Bedankt voor het gebruiken van HangarParkeerder3000")