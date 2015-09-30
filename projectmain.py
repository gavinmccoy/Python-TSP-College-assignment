studentname = "Gavin McCoy"
studentnumber = "D14126655"

print(studentname)
print(studentnumber)

from fromcsvfile import *                   # Using from ... import ... for ease of use
from manualentry import *
from manualentrysix import *

def print_menu():                           # Function prints simple menu for user to choose from.
                                            # Used print("""... instead of several print functions for
                                            # readability.
    print("""
Welcome to the Journey Calculator menu!

Enter "1" to manually enter five airport codes for a given journey OR
Enter "2" to manually enter six airport codes for a given journey OR
Enter "3" to load csv file with airport journeys for various sale reps OR
Enter "4" to exit.
    """)

menuchoice = 0                                          # Had to pick some value for menuchoice, why not 0?!
print_menu()                                            # Prints menu!
while menuchoice != "4":                                # menuchoice not equal to "4" for error handling
    menuchoice = (input("Enter number (1-4): "))        # so nothing but the numbers (or strings in this case)
    if menuchoice == "1":                               # can be entered by the user
        manual_entry()                                  # Turned the main parts of the program into functions
        print_menu()
    elif menuchoice == "2":
        manual_entry_six()
        print_menu()
    elif menuchoice == "3":
        fromcsvfile()
        print_menu()
    elif menuchoice == "4":
        print("Goodbye!")
