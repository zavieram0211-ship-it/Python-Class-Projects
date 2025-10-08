# Speeding
# Zaviera Mitchell
# A program that is given two integers for speed limit, driving speed in mph, and outputs the traffic ticket amount




limit = int(input("Please enter the speed limit for the road: "))
speed = int(input("Please enter the vehicle's recorded speed: "))

# Example: speed limit 50mph 
# 10mph under speed limit receives a $50 ticket

if speed - limit < -10:  # 40mph - 50mph = -10mph
    print("The speeding fine is $50.")
elif speed - limit > 40: # 60mph - 50 mph = 10mph
    print("The speeding fine is $300.")
elif speed - limit > 21: # 75mph - 50mph = 25mph 
    print("The speeding fine is $150.")
elif speed - limit > 6: # 95mph - 50mph = 45 mph
    print("The speeding fine is $75.")
else: 
    print("There is no fine.")


