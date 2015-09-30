from dictionaries import *
from greatcircledist import *
def journeyCost(a, b, c, d, e):
        airport1gps = airportLookupDict.get(a)  # Kept it simple having gps coordinates set up in these
        airport2gps = airportLookupDict.get(b)  # variables
        airport3gps = airportLookupDict.get(c)
        airport4gps = airportLookupDict.get(d)
        airport5gps = airportLookupDict.get(e)
                                                # Currency rates set out below
        airport1currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport1gps[2]))
        airport2currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport2gps[2]))
        airport3currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport3gps[2]))
        airport4currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport4gps[2]))
        airport5currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport5gps[2]))


        # Below is the distance from airport1 to airport 2 multiplied by the currency rate of airport 1 added to
        # the distance to airport2 to airport3 multiplied by currency rate of airport2 and so on...
        # Not forgetting adding the distance from airport5 to airport1 multiplied by the currency of airport 5
        return (getDistanceBetweenCoordinates(float(airport1gps[0]), float(airport1gps[1]),
                                              float(airport2gps[0]), float(airport2gps[1]))) * float(airport1currate) +\
               (getDistanceBetweenCoordinates(float(airport2gps[0]), float(airport2gps[1]),
                                              float(airport3gps[0]), float(airport3gps[1]))) * float(airport2currate) +\
               (getDistanceBetweenCoordinates(float(airport3gps[0]), float(airport3gps[1]),
                                              float(airport4gps[0]), float(airport4gps[1]))) * float(airport3currate) +\
               (getDistanceBetweenCoordinates(float(airport4gps[0]), float(airport4gps[1]),
                                              float(airport5gps[0]), float(airport5gps[1]))) * float(airport4currate) +\
               (getDistanceBetweenCoordinates(float(airport5gps[0]), float(airport5gps[1]),
                                              float(airport1gps[0]), float(airport1gps[1]))) * float(airport5currate)

def journeyCostSix(a, b, c, d, e, f):
        airport1gps = airportLookupDict.get(a) # Kept it simply by having gps coordinates set up in theses variables
        airport2gps = airportLookupDict.get(b)
        airport3gps = airportLookupDict.get(c)
        airport4gps = airportLookupDict.get(d)
        airport5gps = airportLookupDict.get(e)
        airport6gps = airportLookupDict.get(f)
                                                    # Currency rates set out below
        airport1currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport1gps[2]))
        airport2currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport2gps[2]))
        airport3currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport3gps[2]))
        airport4currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport4gps[2]))
        airport5currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport5gps[2]))
        airport6currate = currencyRatesLookupDict.get(countryCurrencyLookupDict.get(airport6gps[2]))


        # Below is the distance from airport1 to airport 2 multiplied by the currency rate of airport 1 added to
        # the distance to airport2 to airport3 multiplied by currency rate of airport2 and so on...
        # Not forgetting adding the distance from airport5 to airport1 multiplied by the currency of airport 5
        return (getDistanceBetweenCoordinates(float(airport1gps[0]), float(airport1gps[1]),
                                              float(airport2gps[0]), float(airport2gps[1]))) * float(airport1currate) +\
               (getDistanceBetweenCoordinates(float(airport2gps[0]), float(airport2gps[1]),
                                              float(airport3gps[0]), float(airport3gps[1]))) * float(airport2currate) +\
               (getDistanceBetweenCoordinates(float(airport3gps[0]), float(airport3gps[1]),
                                              float(airport4gps[0]), float(airport4gps[1]))) * float(airport3currate) +\
               (getDistanceBetweenCoordinates(float(airport4gps[0]), float(airport4gps[1]),
                                              float(airport5gps[0]), float(airport5gps[1]))) * float(airport4currate) +\
               (getDistanceBetweenCoordinates(float(airport5gps[0]), float(airport5gps[1]),
                                              float(airport6gps[0]), float(airport6gps[1]))) * float(airport5currate) +\
               (getDistanceBetweenCoordinates(float(airport6gps[0]), float(airport6gps[1]),
                                              float(airport1gps[0]), float(airport1gps[1]))) * float(airport6currate)
