# Food
# Zaviera Mitchell
# Simulates a point of sale device for a restaurant


# ANSI escape codes for formatting
UNDERLINE = "\033[4m"
RESET = "\033[0m"

menu = {
    "Hot Dog": 1.5,
    "Slice of Pizza": 1.99,
    "Whole Pizza": 9.95,
    "Chicken Bake": 3.99,
    "Soft Drink": 0.69,
    "Ice Cream Sundae": 2.49,
}

price1 = menu["Hot Dog"]
price2= menu["Slice of Pizza"]
price3 = menu["Whole Pizza"]
price4 = menu["Chicken Bake"]
price5 = menu["Soft Drink"]
price6 = menu["Ice Cream Sundae"]
print(f"{UNDERLINE}Menu{RESET}\n")
print(f"1. Hot Dog - ${price1:.2f}")
print(f"2. Slice of Pizza - ${price2:.2f}")
print(f"3. Whole Pizza - ${price3:.2f}")
print(f"4. Chicken Bake - ${price4:.2f}")
print(f"5. Soft Drink - ${price5:.2f}")
print(f"6. Ice Cream Sundae - ${price6:.2f}\n")
hot_dog = (int(input("Please enter the number of Hot Dogs: "))) * menu["Hot Dog"]
slice_pizza = int(input("Please enter the number of Pizza Slices: ")) * menu["Slice of Pizza"]
whole_pizza = (int(input("Please enter the number of Whole Pizzas: "))) * menu["Whole Pizza"]
chicken_bake = (int(input("Please enter the number of Chicken Bakes: "))) * menu["Chicken Bake"]
soft_drink = (int(input("Please enter the number of Soft Drinks: "))) * menu["Soft Drink"]
ice_cream_sundae = (int(input("Please enter the number of Ice Cream Sundaes: "))) * menu["Ice Cream Sundae"]
total = hot_dog + slice_pizza + whole_pizza + chicken_bake + soft_drink + ice_cream_sundae

print(f"The total cost of the order is ${total:.2f}")
      