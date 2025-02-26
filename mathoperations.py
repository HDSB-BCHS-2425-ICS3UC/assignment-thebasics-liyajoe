# Author: Liya Zhou
# Date Modified: February 26, 2025
# Description: 

#Letting Python know I want to use functions from their math library
import math

#Defining variables and adding math functions to them
addition = 2+17 #Finds the sum of the provided numbers
subtraction = 16-5 #Finds the difference of the provided numbers
multiplication = 6*4 #Finds the product of the provided numbers
division = 8/2 #Finds the quotient of the provided numbers
modulus = 20%6 #Finds the remainder after dividing the provided numbers
exponent = 2**4 #Multiplies the first number by itself (second number) times
square_root = math.sqrt(9) #Finds what number you would have to multiply twice to obtain the inputed number

#Prints all variables to the screen while explaining what math operations are used
print(f"Here are some different math operations in Python!\n")
print(f"Addition is 2+17, and that equals {addition}!")
print(f"Subtraction is 16-5, and that equals {subtraction}!")
print(f"Multiplication is 6x4, and that equals {multiplication}!")
print(f"Division is 8/2, and that equals {division}!")
print(f"Modulus is 20%6 (this is basically the remainder!), and that equals {modulus}!")
print(f"An exponent is 2^4, and that equals {exponent}!")
print(f"A square root is √9, and that equals {square_root}!")