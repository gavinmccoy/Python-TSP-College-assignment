import unittest
from greatcircledist import *
from journeycost import journeyCost, journeyCostSix, airportLookupDict, countryCurrencyLookupDict, currencyRatesLookupDict


class TestingMethodsandDictionaries(unittest.TestCase):

#Makes sure the distance from airport to airport formula stays intact
    def test_greatcircletest(self): #JFK to DUB is 5104.628713706877km
        self.assertEqual(getDistanceBetweenCoordinates(40.639751, -73.778925, 53.421333,-6.270075), 5104.628713706877)

#Makes sure the journey cost formula stays intact
    def test_journeycost(self): #DUB to JFK to LAX to SYD to SIN back to DUB costs 32542.107581070813 euros
        self.assertEqual(journeyCost("DUB", "JFK", "LAX", "SYD", "SIN"), 32542.107581070813)

#Makes sure the journey cost formula for six airports stays intact
    def test_journeycostsix(self): #DUB to JFK to LAX to SYD to SIN to CDG back to DUB costs 32996.83440667012 euros
        self.assertEqual(journeyCostSix("DUB", "JFK", "LAX", "SYD", "SIN", "CDG"), 32996.83440667012)

#Makes sure the airport lookup dictionary stays intact
    def test_airportdict(self): #Looking up "DUB" in airportLookupDict gives ('53.421333', '-6.270075', 'Ireland')
        self.assertEqual(airportLookupDict.get("DUB"), ('53.421333', '-6.270075', 'Ireland', 'Dublin'))

#Makes sure the country currency lookup dictionary stays intact
    def test_countrycurr(self): #Looking up "Ireland" in countryCurrencyLookupDict gives 'EUR'
        self.assertEqual(countryCurrencyLookupDict.get("Ireland"), 'EUR')

#Makes sure the currency rate lookup dictionary stays intact
    def test_currrate(self): #Looking up "USD" in currencyRatesLookupDict gives 0.9488
        self.assertEqual(currencyRatesLookupDict.get('USD'), 0.9488)


if __name__ == '__main__':
    unittest.main()