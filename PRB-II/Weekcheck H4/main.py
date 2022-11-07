hangarList = [
  {
    'num': 10,
    'occupied': False
  },
  {
    'num': 11,
    'occupied': False
  },
  {
    'num': 12,
    'occupied': True
  },
  {
    'num': 13,
    'occupied': False
  },
  {
    'num': 14,
    'occupied': False
  },
  {
    'num': 15,
    'occupied': True
  },
  {
    'num': 16,
    'occupied': True
  },
  {
    'num': 17,
    'occupied': False
  },
  {
    'num': 18,
    'occupied': False
  },
  {
    'num': 19,
    'occupied': True
  },
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

print("Welkom bij HangarParkeerder3000")
while True:
  print("-------------------------------------------------")
  print("Deze vliegtuigen wachten om geparkeerd te worden:\n")
  for plane in planeLandedList:
    if plane['hangar'] == 0:
      print(f"{plane['code']}  (type: {plane['type']})")
  planeCode = input("\nPlane code: ")

  print("\nDeze hangars zijn nog vrij:")
  for hangar in hangarList:
    if hangar['occupied'] == False:
      print(f"Hangar {hangar['num']}")
  hangarCode = int(input("\nHanger number: "))

  for plane in planeLandedList:
    if plane['code'] == planeCode:
      plane['hangar'] = hangarCode

  for hangar in hangarList:
    if hangar['num'] == hangarCode:
      hangar['occupied'] = True

  print(f"\nOk, we'll park {plane['code']} in hangar {hangar['num']}!")

  exit = input("\nPress Enter to continue. Type 'X' to quit.\n")
  if exit.lower() == 'x':
    break
