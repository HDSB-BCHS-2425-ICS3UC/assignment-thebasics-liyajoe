#Author: Liya Zhou
#Date Modified: February 28, 2025
#Description: Calculates the volume of a cube, sphere, cpne, or cylinder

#Telling the user what the program can do, and what shapes it can calculate the volume for
print("I will calculate the volume of a shape for you! What shape do you want?")
print("1. Cube")
print("2. Sphere") 
print("3. Cylinder") 
print("4. Cone") 

#Allowing the user to choose the shape they want
choice = input("Type the desired shape's number: ")

#Calculates the volume if the user chose a cube
if choice == "1":
    #The user inputs the dimensions
    side = float(input("What is the length of a side of the cube? ")) 
    #Calculates the volume from the user's input
    volume = side ** 3 
    #Tells the user the final calculated value
    print(f"The volume of the cube is: {volume} cubic units") 

#Calculates the volume if the user chose a sphere
elif choice == "2":
    #Same function as the first 'if' statement 
    radius = float(input("Enter the radius of the sphere: ")) 
    volume = 4/3 * 3.1416 * radius ** 3 
    print(f"The volume of the sphere is: {volume} cubic units") 

#Calculates the volume if the user chose a cylinder
elif choice == "3": 
    #Same function as the first 'if' statement 
    radius = float(input("Enter the radius of the cylinder: ")) 
    height = float(input("Enter the height of the cylinder: ")) 
    volume = 3.1416 * radius ** 2 * height 
    print(f"The volume of the cylinder is: {volume} cubic units") 

#Calculates the volume if the user chose a cone
elif choice == "4": 
    #Same function as the first 'if' statement
    radius = float(input("Enter the radius of the cone: ")) 
    height = float(input("Enter the height of the cone: ")) 
    volume = 1/3 * 3.1416 * radius ** 2 * height 
    print(f"The volume of the cone is: {volume} cubic units") 

#Tells the user to input a new value if they entered an invalid number
else: 
    print("Try again. Make sure the number is one of the provided numbers.")