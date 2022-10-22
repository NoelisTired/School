pilootName = str(input("Naam Piloot\n"))
planeType = str(input("Type Vliegtuig\n"))
currentHeight = int(input("Vlieghoogte\n"))
desiredHeight = int(input("Gewenste Vlieghoogte\n"))
turbulenceExpected = str(input("Turbulentie verwacht? (ja/nee)\n"))
flightDuration = int(input("Vluchtduur\n"))
destination = str(input("Bestemming\n"))
destinationTime = int(input("Aankomsttijd\n"))
pointOfInterest = str(input("Punt van belang\n"))
weatherConditions = str(input("Weersomstandigheden\n"))
clearWeather = str(input("Helder Weer? (ja/nee)\n"))
weatherConditionsArrival = str(input("Weersomstandigheden bij aankomst\n"))
degrees = str(input("Temperatuur\n"))
print(
f"""
Good evening Ladies & gentlemen. this is {pilootName}, your captain for this flight. Here is some information about the flight process.
Our {planeType} is presently climbing trough {currentHeight} feet en route to our cruising altitude of {desiredHeight} so we can expect a climb of {str(desiredHeight - currentHeight)}. We are expecting a {lambda:#!! :} and our flight plan shows an en route time of %s.
We expect to arrive in %s at %s. Our route today will take us over the %s visible on the left-hand side of the aircraft.
The en route weather is %s.=, #EDIT#. The %s weather is %s and about %s degrees Celcius. Enjoy your flight.
"""
)
