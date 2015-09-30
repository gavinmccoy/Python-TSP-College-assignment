#Using from ... import ... instead of just import so I do not have to use e.g. math.sin
from itertools import permutations
from journeycost import *
def fromcsvfile(): #A function to read from a (csv) file for a maximum of four salespeople.

    while True:
        inputfile = input("Type in filename (if I were you I'd try exampleinput.csv): ")
        try:# Puts all of the csv file into a indexed type.
             salespeople = [row for row in csv.reader(open(inputfile))]
        except FileNotFoundError:
            print("File not found.  Have another gander...")
        else:
            break



    alice = salespeople[0][0]                       # For alice or first salesperson in csv file
    aliceairports = salespeople[0][1:6]             # All of that salesperson's airports

    bob = salespeople[1][0]                         # For bob or first salesperson in csv file
    bobairports = salespeople[1][1:6]               # All of that salesperson's airports

    tom = salespeople[2][0]                         # For tom or first salesperson in csv file
    tomairports = salespeople[2][1:6]               # All of that salesperson's airports

    jane = salespeople[3][0]                        # For jane or first salesperson in csv file
    janeairports = salespeople[3][1:6]              # All of that salesperson's airports

    airports = aliceairports
    airportCombinations = []                        # Created a blank list
    for x in permutations(airports):                # For every 5 airport list in all 120 permutations
        airportCombinations.append(list(x) + [x[0]])# add on to that list the first item of every list
                                                    # to the end of the list, making a list of 120 lists of 6 airports
    journeyCostDict = {}                            # where the first and last airports are the same.
    for x in airportCombinations:
        key = journeyCost(x[0], x[1], x[2], x[3], x[4]) # This is a dictionary that stores the 120 permutations
        journeyCostDict[key] = x                        # with the cost as the key so that when the min function
                                                        # is used, it finds the cheapest journey and then looking
                                                        # up the cheapest journey finds the airports

    print("The most cost effective journey for {} is from {} to {} to {} to {} to {} back to {}".format(alice,journeyCostDict.get(min(journeyCostDict))[0],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[1],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[2],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[3],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[4],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[0]))
    print("And it costs: {:.2f} euros".format(min(journeyCostDict)))

    airports = bobairports
    airportCombinations = []
    for x in permutations(airports):
        airportCombinations.append(list(x) + [x[0]])

    journeyCostDict = {}
    for x in airportCombinations:
        key = journeyCost(x[0], x[1], x[2], x[3], x[4])
        journeyCostDict[key] = x



                                                            # Prints out the airports in the cheapest routes
                                                            # by using the cheapest cost and then looking
                                                            # that up in the journey cost dictionary
    print("The most cost effective journey for {} is from {} to {} to {} to {} to {} back to {}".format(bob,journeyCostDict.get(min(journeyCostDict))[0],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[1],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[2],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[3],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[4],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[0]))
                                                            # Unfortunately the above code is hardcoded again and again
                                                            # for the other three salesperson
    print("And it costs: {:.2f} euros".format(min(journeyCostDict)))

    airports = tomairports
    airportCombinations = []
    for x in permutations(airports):
        airportCombinations.append(list(x) + [x[0]])

    journeyCostDict = {}
    for x in airportCombinations:
        key = journeyCost(x[0], x[1], x[2], x[3], x[4])
        journeyCostDict[key] = x




    print("The most cost effective journey for {} is from {} to {} to {} to {} to {} back to {}".format(tom,journeyCostDict.get(min(journeyCostDict))[0],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[1],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[2],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[3],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[4],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[0]))
    print("And it costs: {:.2f} euros".format(min(journeyCostDict)))

    airports = janeairports
    airportCombinations = []
    for x in permutations(airports):
        airportCombinations.append(list(x) + [x[0]])

    journeyCostDict = {}
    for x in airportCombinations:
        key = journeyCost(x[0], x[1], x[2], x[3], x[4])
        journeyCostDict[key] = x




    print("The most cost effective journey for {} is from {} to {} to {} to {} to {} back to {}".format(jane,journeyCostDict.get(min(journeyCostDict))[0],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[1],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[2],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[3],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[4],
                                                                                                 journeyCostDict.get(min(journeyCostDict))[0]))
    print("And it costs: {:.2f} euros".format(min(journeyCostDict)))