# Assignment 4
# Carina Luo

from Airport import *  # Import Airport class and it's functions


class Flight:
    """This is the flight class."""

    def __init__(self, flightNo, origin, destination):
        if isinstance(origin, Airport) and isinstance(destination, Airport):    # If the origin and destination
            # are Airport objects, define the attributes
            self._flightNo = flightNo
            self._origin = origin
            self._destination = destination
        else:
            raise TypeError(f'The origin and destination must be Airport objects')

    def getFlightNumber(self):
        return self._flightNo

    def getOrigin(self):
        return self._origin

    def getDestination(self):
        return self._destination

    def isDomesticFlight(self):
        if self._origin.getCountry() == self._destination.getCountry():
            return True
        else:
            return False

    def setOrigin(self, origin):
        self._origin = origin

    def setDestination(self, destination):
        self._destination = destination

    def __repr__(self):
        if self.isDomesticFlight():
            typeFlight = str('{domestic}')
        else:
            typeFlight = str('{international}')

        return f'Flight: {self._flightNo} from {self._origin.getCity()} to {self._destination.getCity()} {typeFlight}'

    def __eq__(self, other):
        return self._origin == other.getOrigin() and self._destination == other.getDestination()
