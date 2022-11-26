import os
pilotList = ["Bob", "John", "Fred", "Marie", "Jack", "Bill"]

#! Onnodige global nameToGreet heb ik weggehaald. Je kunt deze gewoon in de functie definiëren, dat is veel netter. en past beter bij de opdracht

while True:
    [print(pilot) for pilot in pilotList]
    nameToGreet = input("\nVoer een naam in (of 'exit' om te stoppen):\n")
    if(nameToGreet == None):
        print("Voer een naam in!\n")
        continue
    if(nameToGreet == "exit"):
        break
    for pilot in pilotList:
        if nameToGreet == pilot:
            print("Hallo %s, welkom terug!" % nameToGreet)
        else:
            print(pilot)
    os.system('cls')
