# Using from ... import ... instead of just import so I do not have to use e.g. math.sin
from itertools import permutations
from journeycost import *


def manual_entry():
    # Below takes the user's input for each airport
    # Errors are prevented from happening by making sure the airport code is three characters long,
    # made up of alphabetic characters and is in the airport lookup dictionary.
    # All characters, once they have satisfied all of the above conditions
    # are then forced to uppercase as that is the kind of case that
    # the airport lookup dictionary likes.
    airport1 = ""
    while len(airport1) != 3 or not airport1.isalpha() or airport1 not in airportLookupDict:
        airport1 = input("Enter valid code for first airport please: ").upper()
    print("Airport stored.")

    airport2 = ""
    while len(airport2) != 3 or not airport2.isalpha() or airport2 not in airportLookupDict or (airport2 == airport1):
        airport2 = input("Enter valid code for second airport please: ").upper()
    print("Airport stored.")

    airport3 = ""
    while len(airport3) != 3 or not airport3.isalpha() or airport3 not in airportLookupDict or (airport3 == airport1) \
            or (airport3 == airport2):
        airport3 = input("Enter valid code for third airport please: ").upper()
    print("Airport stored.")

    airport4 = ""
    while len(airport4) != 3 or not airport4.isalpha() or airport4 not in airportLookupDict or (airport4 == airport1) \
            or (airport4 == airport2) or (airport4 == airport3):
        airport4 = input("Enter valid code for fourth airport please: ").upper()
    print("Airport stored.")

    airport5 = ""
    while len(airport5) != 3 or not airport5.isalpha() or airport5 not in airportLookupDict or (airport5 == airport1) \
            or (airport5 == airport2) or (airport5 == airport3) or (airport5 == airport4):
        airport5 = input("Enter valid code for fifth airport please: ").upper()
    print("Airport stored.")

                                                            # Added all the airports into a list to get
                                                            # ready to permutate them.
    airports = [airport1, airport2, airport3, airport4, airport5]

    airportCombinations = []                                # Created a blank list
    for x in permutations(airports):                        # For every 5 airport list in all 120 permutations
        airportCombinations.append(list(x) + [x[0]])        # add on to that list the first item of every list
                                                            # to the end of the list, making a list of 120 lists of 6 airports
    journeyCostDict = {}                                    # where the first and last airports are the same.
    for x in airportCombinations:
        key = journeyCost(x[0], x[1], x[2], x[3], x[4])     # This is a dictionary that stores the 120 permutations
        journeyCostDict[key] = x                            # with the cost as the key so that when the min function
                                                            # is used, it finds the cheapest journey and then looking
    print()                                                 # up the cheapest journey finds the airports

                                                            # airportXfull helps to get the full length name of the
                                                            # airport from the lowest costing permutated journey
                                                            # for printing purposes later on
    airport1full = airportLookupDict.get(journeyCostDict.get(min(journeyCostDict))[0])[3]
    airport2full = airportLookupDict.get(journeyCostDict.get(min(journeyCostDict))[1])[3]
    airport3full = airportLookupDict.get(journeyCostDict.get(min(journeyCostDict))[2])[3]
    airport4full = airportLookupDict.get(journeyCostDict.get(min(journeyCostDict))[3])[3]
    airport5full = airportLookupDict.get(journeyCostDict.get(min(journeyCostDict))[4])[3]

                                                            # Prints out the airports in the cheapest routes
                                                            # by using the cheapest cost and then looking
                                                            # that up in the journey cost dictionary
    print("The most cost effective journey is from {} to {} to {} to {} to {} back to {}"
          .format(journeyCostDict.get(min(journeyCostDict))[0], journeyCostDict.get(min(journeyCostDict))[1],
                  journeyCostDict.get(min(journeyCostDict))[2], journeyCostDict.get(min(journeyCostDict))[3],
                  journeyCostDict.get(min(journeyCostDict))[4], journeyCostDict.get(min(journeyCostDict))[0]))

                                                            # Put the cost in "euros" instead of using the euro
                                                            # symbol to ensure widespread compatibility.
                                                            # Rounded the price to two decimal places for a real
                                                            # world feel.
    print("And it costs: {:.2f} euros".format(min(journeyCostDict)))

    print("Here's a handy card of your itinerary for you to print out: ")

    print("""
    Airport No.             Airport Name
        1                   {}
        2                   {}
        3                   {}
        4                   {}
        5                   {}
        6                   {}
    Total Cost              {:.2f} Euros
    """.format(airport1full, airport2full, airport3full, airport4full, airport5full, airport1full,
               min(journeyCostDict)))