# Author: Liya Zhou
# Date Modified: February 27, 2025
# Description: Finds the discriminant (the number of solutions in a quadratic)

#Telling the user what the code does for UX
print("Here is code that will find the discriminant of a quadratic function...")

#Storing the user's input in variables with one second time increments in between
a = float(input("What is your 'a' value?\nType here: "))
b = float(input("Cool! What is your 'b' value?\nType here:"))
c = float(input("Lastly, what is your 'c' value?\nType here:"))

#Calculating the discriminant from the inputed values
discriminant = b**2 - 4*a*c

#Printing the discriminant to the screen
print(f"Thanks! Your discriminant is {discriminant}.")