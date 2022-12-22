# Assignment 4
# Carina Luo

class Airport:
    """This is the Airport class."""

    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    def __repr__(self):
        return f'{self._code}({self._city}, {self._country})'  # This is the repr

    def getCode(self):
        return self._code

    def getCity(self):
        return self._city

    def getCountry(self):
        return self._country

    def setCity(self, city):
        self._city = city

    def setCountry(self, country):
        self._country = country

