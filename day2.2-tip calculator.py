print("Welcome to the tip calculator!\n")
totalbill = int(input("What was the total bill? $"))
split = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 5 or 10? "))
calc = totalbill//split
calc1 = float(calc+calc*(tip/100))

print("Each person should pay $" + str(calc1) )
