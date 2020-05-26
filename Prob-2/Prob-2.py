# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Eddy

# calculates the change from a transaction and prints out the number of each denomination for the change

# function definition


# main function definition

from math import *

# my first attempt
"""
def whatsCost():
    totalCost = input("what is the amount due?: ")
    payed = input("How much did they pay?: ")


def math(totalCost, payed):
    change = (payed) - (totalCost)


def sum():
    print(math)
"""


# after watching the help video trying to take notes
"""
change = 19.99
# converts it to an int
print("change:", change)
print("change * 100:", change * 100)
print("rounded change:", round(change))
changeDue = int(round(change * 100))
print("change due:", changeDue)
# calculate number of tens
tens = changeDue // 100
if tens >= 1:
    print("tens:", tens)
# adjust changeDue to refelct change given
changeDue = changeDue - (tens * 1000)
print("change due:", changeDue)

# calculate number of fives
fives = changeDue // 500
if fives >= 1:
    print("fives:", fives)
# adjust changeDue
changeDue = changeDue - (fives * 500)
"""


def money():
    totalCost = input("what is the cost: ")
    payed = input("what was payed: ")


def changeDue(totalCost, payed):
    money()

    amountdue = totalCost - payed
    change = (round(amountdue*100))
    tens = change//100
    if tens >= 1:
        print("tens:", tens)
    change = change-(tens*1000)
    # fives
    fives = change//500
    if fives >= 1:
        print("fives:", fives)
    change = change-(fives*500)
    # ones
    ones = change//100
    if ones >= 1:
        print("ones:", ones)
    change = change-(ones*100)
    # quarters
    quarters = change//25
    if quarters >= 1:
        print("quaters:", quarters)
    change = change-(quarters*25)
    # dimes
    dimes = change // 10
    if dimes >= 1:
        print("dimes:", dimes)
    change = change-(dimes*10)
    # nickles
    nickles = change // 5
    if nickles >= 1:
        print("nickles:", nickles)
    change = change-(nickles*5)
    # pennys
    pennys = change // 1
    if pennys > 1:
        print("pennys:", pennys)
    change = change-(pennys*1)


changeDue()
