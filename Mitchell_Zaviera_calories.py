#Calories
#Zaviera Mitchell
#This program finds the amount of calories a person burns


Age = float(input("Please enter your age: "))
weight = float(input("Please enter your weight in pounds: "))
heart_rate = float(input("Please enter your heart rate in beats per minute: "))
time = float(input("Please enter the length of your workout in minutes: "))

# Math Equation

Calories_burned = (Age*0.2757 + weight*0.03295 + heart_rate*1.0781 - 75.4991) *time / 8.368

print(f"Calories_burned: {Calories_burned: .2f}")