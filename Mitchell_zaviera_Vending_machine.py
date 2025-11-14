# Zaviera Mitchell
# Program: Vending Machine
# Purpose: Simulates how a vending machine functions

class VendingMachine:
    # A constuctor for Vending Machine class
    def __init__(self, soda, coffee, water):
        self.soda = soda
        self.coffee = coffee
        self.water = water

    # Purchase of specified drink in vending Machine if available
    # Subtract 1 of specific drink if user purchases that drink
    def buy_drink(self, drink_type):

        if drink_type == 1:
            if self.soda > 0:   # Checks if soda is in stock
                self.soda -= 1  # Subtracts 1 soda from inventory
                print("You've successfully purchased a soda. Enjoy!")
            else:
                print("Sorry, our soda is out of stock")
        elif drink_type == 2:
            if self.coffee > 0:  # Checks if coffee is in stock
                self.coffee -= 1 # Subtracts 1 coffee from inventory
                print("You've successfully purchased a coffee. Enjoy!")
            else:
                print("Sorry, our coffee is out of stock.")
        elif drink_type == 3:
            if self.water > 0:  # Checks if water is in stock
                self.water -= 1  # Subtracts 1 water from inventory
                print("You've successfully purchased a water. Enjoy!")
            else:
                print("Sorry, our water is out of stock.")
            
        else:  # Handles invalid drink type input (only 1, 2, or 3 accepted)
            print("Invalid drink: please select soda, coffee, or water")


    # Restocks whatever beverage chosen by user by specified amount
    def restock(self, drink_type, amount):
        if amount < 0:  # Validates positive restock amount (Cannot restock negative amount)
            print("Invalid: Input a positive number to restock!")
            return
        if drink_type == 1:
            self.soda += amount    # Restocks soda by specified amount
            print(f"soda restocked by {amount}.")
        elif drink_type == 2:
            self.coffee += amount  # Restocks coffee by specified amount
            print(f"coffee restocked by {amount}.")
        elif drink_type == 3:
            self.water += amount   # Restocks water by specified amount
            print(f"water restocked by {amount}.")
        else:  # Handles invalid drink type input (only 1, 2, or 3 accepted)
            print("Invalid drink type, please select soda, coffee, or water")

    # Reports current inventory of all drinks in vending machine
    def report(self):
        print("Inventory")
        print(f"Soda: {self.soda} bottles")
        print(f"Coffee: {self.coffee} bottles")
        print(f"Water: {self.water} bottles")

# Main function to run vending machine simulation
def main():
    vm = VendingMachine(10, 10, 10) # Initializing vending machine with 10 of each drink
    stopwords = ["q", "quit"]       # Commands to exit the program
    buy = ['b', 'buy']              # Commands to buy a drink
    restock = ['r', 'restock']      # Commands to restock a drink
    inventory = ['i', 'inventory']  # Commands to view inventory
    go = True                       # Control variable for main loop

    # Main loop for user interaction
    while(go):

        print("\nWelcome to the Vending Machine!")
        print("Please select an option:")
        print("------------------------")
        print("Would you like to\nB-Buy\nR-Restock\nI-Inventory\nQ-Quit")  

        user_input = input(":> ")
        if user_input.lower() in stopwords:
            go = False    # Exits the loop and ends the program
            print("Goodbye!")
            break         # Exits the program (Ensures previous code does not run)

        elif user_input in buy:                 # Prompts user to select drink to buy
            print("Please select an option: ")
            print("------------------------")
            print("1-Soda\n2-Coffee\n3-Water")
            num = int(input(":> "))           # Gets user input for drink choice
            if num > 0 and num <= 3:            # Validates drink choice input (only 1, 2, or 3 accepted)
                vm.buy_drink(num)               # Calls buy_drink method to process purchase
                continue                        # Continues to next iteration of loop
            else:
                print("Invalid Input")
        elif user_input.lower() in restock:     # Prompts user to select drink to restock
            print("Please select an option: ")
            print("------------------------")
            print("1-Soda\n2-Coffee\n3-Water")
            num = int(input(":> "))
            if num > 0 and num <= 3:                            # Validates drink choice input (only 1, 2, or 3 accepted)
                amount = int(input("Please enter an amount: ")) # Gets user input for restock amount
                vm.restock(num, amount)                         # Calls restock method to process restock   
            else:
                print("Invalid Option")
        elif user_input.lower() in inventory:                   # Calls report method to display current inventory
            vm.report()






if __name__ == "__main__":
    main()







