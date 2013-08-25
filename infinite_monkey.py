#-------------------------------------------------------------------------------
# Name:        infinite_monkey
# Purpose:
#
# Author:      Ed Hunter
#
# Created:     25/08/2013

#-------------------------------------------------------------------------------

import random
import time

lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','X', ' ', '1','2','3','4','5','6','7','8,','9','!','@','#','$','%','^','&','*','(',')','-', '_', '=', '+', '[',']', '{', '}', '|', ';', '"', "'", ',', '.','/', '<', '>', '?', '`', '~']

print("This program randomly generates letters, numbers, and symbols until the zeroth index of the string is guessed.  Then it guess the first index and keeps going until entire string is guessed.")
print("My inspiration for this program comes from the infinite monkey theorem.  This program isn't exactly how the theorum works, but it would run for a very long time if it didn't match up the indices.")

tries = 0

def monkey(stringToGuess):
    '''This program randomly generates letters, numbers, and symbols until the zeroth index of the string is guessed.  Then it guess the first index and keeps going until entire string is guessed.  My inspiration for this program comes from the infinite monkey theorem.  This program isn't exactly how the theorum works, but it would run for a very long time if it didn't match up the indices.'''

    randomString = ""
    index = 0
    global tries
    while(stringToGuess != randomString):
        guess = random.randint(0, len(lst)-1)
        tries += 1
        print("String = " + randomString + ", " + "Guess = " + lst[guess])
        if(stringToGuess[index] == lst[guess]):
             randomString += lst[guess]
             index += 1
    return randomString




def start():
    userInput = 'y'
    while(userInput.lower() == 'y'):
        string = input("Enter the string to be randomly guessed.")
        start = time.clock()
        string = monkey(string)
        end = time.clock() - start
        print("The string is " + "'" + string + "'." + "  This took " + str(tries) + " tries" + " and " + str(round(end, 2)) + " seconds to guess.")
        userInput = input("Again, y/n?")

start()

