import csv

f = open('airport.csv', encoding="utf8")                    # Standard csv file reading
csv_f = csv.reader(f, delimiter=",", quotechar='"')
airportLookupDict = {}
for row in csv_f:
    key = row[4]                                            # key is three character airport code e.g. "DUB"
    airportLookupDict[key] = row[6], row[7], row[3], row[1] # Looking that key up gives latitude, longitude, country
f.close()                                                   # and full name of airport

f = open('countrycurrency.csv', encoding="utf8")
csv_f = csv.reader(f, delimiter=",", quotechar='"')
countryCurrencyLookupDict = {}
for row in csv_f:
    key = row[0]                                            # key is country
    countryCurrencyLookupDict[key] = row[14]                # looking that key gives a country's currency code
f.close()

f = open('currencyrates.csv', encoding="utf8")
csv_f = csv.reader(f, delimiter=",", quotechar='"')
currencyRatesLookupDict = {}
for row in csv_f:
    key = row[1]                                            # key is currency code
    currencyRatesLookupDict[key] = float(row[2])            # looking that key up gives the exchange rate to euro
f.close()