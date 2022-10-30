pilotList = ["Bob", "John", "Fred", "Marie", "Jack", "Bill"]
isRunning = True

#! Onnodige global nameToGreet heb ik weggehaald. Je kunt deze gewoon in de functie definiëren, dat is veel netter. en past beter bij de opdracht

while isRunning:
    nameToGreet = input("\nVoer een naam in (of 'X' om te stoppen):\n")
    if(nameToGreet == None):
        print("Voer een naam in!")
        continue
    if(nameToGreet == "exit"):
        isRunning = False
    for pilot in pilotList:
        if nameToGreet == pilot:
            print("Hallo %s, welkom terug!" % nameToGreet)
        else:
            print(pilot) 
