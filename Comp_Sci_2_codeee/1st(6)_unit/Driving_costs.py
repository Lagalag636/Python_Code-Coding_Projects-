#code a function to collect and calculate driving costs.
def driving_cost(miles_driven, miles_per_gallon, dollars_per_gallon):
    cost = round((miles_driven / miles_per_gallon) * dollars_per_gallon, 2)
    if cost < 0:
        raise ValueError("Cost cannot be negative")
    return cost

#greeting call
def greeting():
    print("This program calculates the cost of driving.")
    print("You will be asked to enter the number of miles driven per year,")
    print("the miles per gallon of your car, and the price of a gallon of gas.")
    print("The program will then calculate the cost of driving for the year.")
    print()

#main function
def main():
    greeting()
    miles_driven = float(input("Enter the number of miles for the trip or driven per year: "))
    miles_per_gallon = float(input("Enter the miles per gallon of the car: "))
    dollars_per_gallon = float(input("Enter the average price of a gallon of gas: "))
    cost = driving_cost(miles_driven, miles_per_gallon, dollars_per_gallon)
    print("The cost of driving for the year is $", format(cost, ",.2f"), sep="")

#call main function
if __name__ == "__main__":
    main()