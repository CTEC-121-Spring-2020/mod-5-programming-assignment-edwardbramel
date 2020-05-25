# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Eddy

# a number between 1 and 10 returns a string representing the Roman numeral

# function definition

# unit test function


def romanN(number):
    if number == 1:
        return 'I'
    elif number == 2:
        return 'II'
    elif number == 3:
        return 'III'
    elif number == 4:
        return 'IV'
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8:
        return "VIII"
    elif number == 9:
        return "IX"
    elif number == 10:
        return "X"
    else:
        return "unknown"


def unitTest():
    print("your Roman numeral is: ", romanN(1))
    print("your Roman numeral is: ", romanN(2))
    print("your Roman numeral is: ", romanN(3))
    print("your Roman numeral is: ", romanN(4))
    print("your Roman numeral is: ", romanN(5))
    print("your Roman numeral is: ", romanN(6))
    print("your Roman numeral is: ", romanN(7))
    print("your Roman numeral is: ", romanN(8))
    print("your Roman numeral is: ", romanN(9))
    print("your Roman numeral is: ", romanN(10))
    print("your Roman numeral is: ", romanN(0))
    print()


unitTest()
