"""
Write a program that finds the Discriminant ---- Delta = b^2 – 4ac The output should be

similar to the following ( D ifficulty Mark 3 ):
"""

# Author: Liya Zhou
# Date Modified: February 26, 2025
# Description: Finds the discriminant (the number of solutions in a quadratic)

#Letting the program know I want to use a function from their "time" library
import time

#Telling the user what the code does for UX
print("Here is code that will find the discriminant of a quadratic function...")

#Having the code pause for 2 seconds to let the user register what's happening
time.sleep(1)

#Storing the user's input in variables with one second time increments in between
a = float(input("What is your 'a' value?\nType here: "))
time.sleep(0.5)
b = float(input("Cool! What is your 'b' value?\nType here:"))
time.sleep(0.5)
c = float(input("Lastly, what is your 'c' value?\nType here:"))
time.sleep(0.5)

#Calculating the discriminant from the inputed values
discriminant = b**2 - 4*a*c

#Printing the discriminant to the screen
print(f"Thanks! Your discriminant is {discriminant}.")