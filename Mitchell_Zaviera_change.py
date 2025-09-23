#Zaviera Mitchell
#Change
# Convert number of cents into the fewest number of US coins of that amount


cents = int(input("Please enter number of cents: ")) # cents =48

# Quarters
quarters = cents // 25 # cents = 48, qurters = 1
cents -= quarters * 25 # cents = 23

#Dimes
dimes = cents // 10 # cents = 23, quarters = 1, dimes = 2
cents -= dimes *10 # cents = 3, quarters = 1, dimes = 2

#Nickels
nickels = cents // 5 #cents = 3, quarters = 1, dimes = 2, nickels = 0
cents -= nickels *5  #cents = 3, quarters = 1, dimes = 2, nickels =0

#Pennies
pennies = cents // 1
cents = cents - pennies *1

print("Coins: ", quarters, "quarters", dimes, "dimes", nickels, "nickels", pennies, "pennies")