import math
import random


#Calculate the volume of a Sphere
#Calculate the factorial of a randomly generated number between 1 and 10

input("Please enter the radius of the sphere: ")

#Volume equation

radius = 3
volume = 4/3 * math.pi *3 **3

print(f"The volume of a sphere with the radius of 3 is:  {volume:.2f}")

number = random.randrange(1,11)
factorial = math.factorial(number)

print("The factorial of", number, "is", factorial)
