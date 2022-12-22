
from Flight import *  # Import Flight class, which imports the Airport class as well

allAirports = []
allFlights = {}


def loadData(airportFile, flightFile):
    """Accepts the airport and flight files and adds data to allAirports and allFlights"""
    portsList = []
    flightsList = []
    keysList = []
    flightsContainer = []
    try:
        with open(airportFile, 'r') as airports:
            for line in airports:
                target = line.rstrip()  # remove the newline character
                separate = target.split(",")  # split each attribute by comma
                for i in range(len(separate)):  # for every attribute
                    noSpaces = separate[i].strip()  # remove the whitespaces
                    separate[i] = noSpaces
                portsList.append(separate)  # append to portslist
        for i in range(len(portsList)):
            objTarget = portsList[i]
            port = Airport(objTarget[0], objTarget[2], objTarget[1])  # create the airport object
            allAirports.append(port)  # append to all airports

        with open(flightFile, 'r') as flights:
            for line in flights:
                target = line.rstrip()
                separate = target.split(",")
                for i in range(len(separate)):
                    noSpaces = separate[i].strip()
                    separate[i] = noSpaces
                flightsList.append(separate)  # append attribute of each flight to the flights list
        for i in range(len(flightsList)):
            if flightsList[i][1] not in keysList:
                keysList.append(flightsList[i][1])  # Create a list of keys

        for i in range(len(flightsList)):
            objTarget = flightsList[i]
            fly = Flight(objTarget[0], getAirportByCode(objTarget[1]), getAirportByCode(objTarget[2]))  # create each
            # flight object
            flightsContainer.append(fly)  # append each flight object to a list containing all the flights
            for j in range(len(keysList)):  # for every key in keysList
                everyFlight = []  # create a new list value for each key
                for k in range(len(flightsContainer)):
                    if keysList[j] == flightsContainer[k].getOrigin().getCode():  # if the key corresponds to the
                        # origin code
                        everyFlight.append(flightsContainer[k])  # Append to the value list
                    else:
                        continue
                allFlights[keysList[j]] = everyFlight  # create the allFLights dictionary
        return True

    except Exception:
        return False


def getAirportByCode(code):
    """Returns the airport object when it's code is entered."""
    for i in range(len(allAirports)):  # for every airport
        selectedAirport = allAirports[i].getCode()
        if selectedAirport == code:
            return allAirports[i]  # return the airport object if it's code matches the code entered
        elif selectedAirport != code:
            continue  # continue if the code doesn't match
        else:
            return -1  # if there are no airports that have a corresponding code return -1


def findAllCityFlights(city):
    """Returns a list that contains all the flight objects with a given city"""
    flightCitylist = []
    for key, value in allFlights.items():
        for i in range(len(value)):
            if value[i].getOrigin().getCity() == city or value[i].getDestination().getCity() == city:
                flightCitylist.append(value[i])     # append to the list if a flight object has that city as its
                # attribute
    return flightCitylist


def findAllCountryFlights(country):
    """Returns a list that contains all flight objects with a given country"""
    flightCountrylist = []
    for key, value in allFlights.items():
        for i in range(len(value)):
            if value[i].getOrigin().getCountry() == country or value[i].getDestination().getCountry() == country:
                flightCountrylist.append(value[i])      # append to the list if a flight object has that country as its
                # attribute
    return flightCountrylist


def findFlightBetween(origAirport, destAirport):
    """Returns a direct flight, or a set with airports that provide a flight to the destination,
    or -1 if there are no airports that provide a flight to the destination"""
    originFlights = allFlights[origAirport.getCode()]   # get a list with all the flights from the origin
    transferFlight = []
    indFlight = []
    hopFlights = []
    flightSet = set()
    directStatus = False    # if there is a direct flight
    transferStatus = False  # if there is a transfer available
    for i in range(len(originFlights)):
        if originFlights[i].getDestination() == destAirport:    # if the origin has a direct flight to the destination
            directStatus = True     # set the direct flight status as true
            return f'Direct flight: {origAirport.getCode()} to {destAirport.getCode()}'     # return this string
    if directStatus is False:   # if there are no direct flights
        for i in range(len(originFlights)):     # for all the flights from an origin
            transferFlight.append(originFlights[i].getDestination())    # append the destination airports
        for i in range(len(transferFlight)):    # for all the possible destination airports from the origin
            eachFlight = allFlights[transferFlight[i].getCode()]     # find the flights from those destination airports
            hopFlights.append(eachFlight)   # append the list of flights to the hopFlights list
        for i in range(len(hopFlights)):    # for each list of flights in the hopFlights list
            anyFlight = hopFlights[i]
            for j in range(len(anyFlight)):     # for each individual flight
                indFlight.append(anyFlight[j])   # append to a list
        for i in range(len(indFlight)):
            if indFlight[i].getDestination() == destAirport:    # if the destination for each flight corresponds
                # to the given destination airport
                flightSet.add(indFlight[i].getOrigin().getCode())   # add the airport to a set
        if flightSet != set():  # if the set is not empty
            transferStatus = True
        if transferStatus is True:
            return flightSet    # return the set
        if transferStatus is False and directStatus is False:   # if there are no direct flights and
            # one-stage transfer flights
            return -1


def findReturnFlight(firstFlight):
    """Finds a direct return flight"""
    returnAirport = firstFlight.getDestination().getCode()
    returnFlights = allFlights[returnAirport]   # list with all the flights from the airport
    # we would like to return from
    reAirport = []
    for i in range(len(returnFlights)):
        if returnFlights[i].getDestination() == firstFlight.getOrigin():
            reAirport.append(returnFlights[i])  # append the airport that has a flight back to a list
    if reAirport:   # if the list is not empty
        for i in range(len(reAirport)):
            return reAirport[i]     # return the return flight
    else:   # if there are no direct return flights
        return -1
