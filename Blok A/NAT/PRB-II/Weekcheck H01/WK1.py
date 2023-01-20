pilootName = str(input("Naam Piloot\n"))
planeType = str(input("Type Vliegtuig\n"))
currentHeight = int(input("Vlieghoogte\n"))
desiredHeight = int(input("Gewenste Vlieghoogte\n"))
turbulenceExpected = str(input("Turbulentie verwacht? (ja/nee)\n"))
flightDuration = str(input("Vluchtduur\n"))
destination = str(input("Bestemming\n"))
destinationTime = int(input("Aankomsttijd\n"))
pointOfInterest = str(input("Punt van belang\n"))
weatherConditions = str(input("Weersomstandigheden\n"))
clearWeather = str(input("Helder Weer? (ja/nee)\n"))
weatherConditionsArrival = str(input("Weersomstandigheden bij aankomst\n"))
degrees = str(input("Temperatuur\n"))

#! Overschreven variabel in de volgende regels
if turbulenceExpected.lower() in ['ja', 'j', 'yes', 'y']:
    turbulenceExpected = "bumpy ride"
else:
    turbulenceExpected = "smooth ride"
    
#! Array met alle variabelen
if clearWeather.lower() in ['ja', 'j', 'yes', 'y']:
    clearWeather = "which will give us a chance to poiny out some specific landmarks", True
else:
    clearWeather = "so we will not get to see much of the specific landmarks", False
print(
    f"""
Good evening Ladies & gentlemen. this is {pilootName}, your captain for this flight. Here is some information about the flight process. Our {planeType} is presently climbing trough {currentHeight} feet en route to our cruising altitude of {desiredHeight} so we can expect a climb of {str(desiredHeight - currentHeight)}. We are expecting a {turbulenceExpected} and our flight plan shows an en route time of {flightDuration}. We expect to arrive in {destination} at {destinationTime}. Our route today will take us over the {pointOfInterest} visible on the left-hand side of the aircraft. The en route weather is {f'clear skies' if clearWeather[1] else f'foggy sky'}, {clearWeather[0]}. The {destination} weather is {weatherConditionsArrival} and about {degrees} degrees Celcius. Enjoy your flight.
"""
)
