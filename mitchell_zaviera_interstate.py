# Program: Interstate Highways
# Author: Zaviera Mitchell
# Purpose: To determine if a highway number is valid, primary, or auxilary,
#          and to determine the direction of travels.



highway_num = int(input("Please enter an interstate number: "))


# Handled Invalid Highways 00 or above 999
if(highway_num < 1 or highway_num > 999 or highway_num%100 ==0): 
    print(highway_num, 'is not a valid interstate highway number.')

# primary highways (1-99)

elif (highway_num <= 99):
    print("Highway is Primary, ")
    if highway_num %2 ==0: 
        print(f"I-{highway_num} going East/West") #Even numbers are east/west
    else:
        print(f"I-{highway_num} going North/South") #Odd numbers are north/south
else:
    # Auxiliary highways (100-999 excluding endings with 00's)
    
    served = highway_num%100

    if served%2 ==0: 
        print(f"Highway is Auxiliary, Primary highway it is serving is I-{served}, going East/West.")
    else:
        print(f"Highway is Auxiliary, Primary highway it is serving is I-{served}, going North/South.")


