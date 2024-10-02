# Programmers: Theresa DeJacimo and Paige Ronan
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/25/2024
# Lab Assignment: 1
# Problem Statement: [figure out the cost for gas for your trip using
# how many miles you will travel, the miles per gallon (MPG)
# of your car, and the cost of gas.]
# Data In: miles being traveled, miles per gallon, price per gallon
# Data Out: total cost of gas
# Credits: [in class]


#Ask how many miles user is traveling
miles_int = int(input("How many miles are you traveling?"))

#Ask how many miles one gallon fuels for
mpg_int = int(input("How many miles per gallon?"))

#Ask how much one gallon of gas costs
gallon_cost_int = int(input("How much does 1 gallon cost?"))

gallon_num = miles_int / mpg_int

total_cost = gallon_cost_int * gallon_num

print(f'Total cost: {total_cost:.2f}')

