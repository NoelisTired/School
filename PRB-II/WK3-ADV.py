import os

hangarList = [
  {'num': 10, 'occupied': False},
  {'num': 11, 'occupied': False},
  {'num': 12, 'occupied': True},
  {'num': 13, 'occupied': False},
  {'num': 14, 'occupied': False},
  {'num': 15, 'occupied': True},
  {'num': 16, 'occupied': True},
  {'num': 17, 'occupied': False},
  {'num': 18, 'occupied': False},
  {'num': 19, 'occupied': True},
]
planeLandedList = [
  {
    'code': 'ACV1',
    'type': 'Airbus A123',
    'capacity': 853,
    'hangar': 0
  },
  {
    'code': 'GOR7',
    'type': 'Boeing 909',
    'capacity': 110,
    'hangar': 0
  },
  {
    'code': 'QEN4',
    'type': 'Fokker X888',
    'capacity': 530,
    'hangar': 0
  },
  {
    'code': 'TOV2',
    'type': 'Airbus X303',
    'capacity': 495,
    'hangar': 0
  },
]

#? ENTRY POINT
if __name__ == "__main__":
    while True:
        if os.name == 'nt': #? Windows
            os.system('cls')
        else:
            os.system('clear') #? Linux
        print("Welkom bij HangarParkeerder3000")
        for plane in planeLandedList:
            if plane['hangar'] == 0:
                print("> Vliegtuig %s is nog niet geplaatst in een hangar" % plane['code'])
        for hangar in hangarList:
            if not hangar['occupied']:
                print("- Hangar %s is beschikbaar" % hangar['num'])
        input("")

    # isRunning = True

    # while isRunning:
    #     print("-------------------------------------------------")
    #     print("Deze vliegtuigen wachten om geparkeerd te worden:")