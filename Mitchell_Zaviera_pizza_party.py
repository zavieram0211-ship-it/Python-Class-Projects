#Variables
number_of_people = int(input("Please enter the number of people attenting the party: "))
number_of_pizzas = int(input("Please enter the number of pizzas purchased for the party: "))
diameter_of_each_pizza = int(input("Please enter the diameter of the pizzas: "))
slices_per_pizza= int(input("Please enter the number of slices per pizza: "))

#Math

radius= diameter_of_each_pizza/2
area_of_one_pizza= 3.14*radius*radius

Total_pizza_area= area_of_one_pizza*number_of_pizzas
Total_number_of_pizza_slices= slices_per_pizza*number_of_pizzas
pizza_area_per_person= Total_pizza_area/number_of_people
slices_per_person= Total_number_of_pizza_slices/number_of_people






print("Total pizza area: ", Total_pizza_area, "square inches")
print("Total number of pizza slices: ", Total_number_of_pizza_slices)
print(f"Pizza area per person: {pizza_area_per_person:.2f} spuare inches")
print(f"Slices per person: {slices_per_person:.2f}")