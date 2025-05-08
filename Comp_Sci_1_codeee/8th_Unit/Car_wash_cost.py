service_titles = [
    ("Automated Car Wash", 1),
    ("Basic Vacuuming", 3),
    ("Windows Cleaning", 4),
    ("Tire and Wheel Cleaning", 5),
    ("Full Interior Detailing", 6),
    ("Exterior Waxing and Polishing", 7),
    ("Clay Bar Treatment", 8),
    ("Engine Bay Cleaning", 9),
    ("Paint Restoration", 10),
    ("Scratch and Swirl Removal", 11),
    ("Odor Removal", 12),
    ("Pet Hair Removal", 13),
    ("Rain Repellent Application", 14),
    ("Underbody Wash", 15),
    ("Fleet Washing", 2),
]

payment = []

car_wash_services = {
    1: {
        "title": "Automated Car Wash",
        "description": "Drive-through car wash with automated cleaning equipment.",
        "price": 10.00,
    },
    2: {
        "title": "Fleet Washing",
        "description": "Cleaning multiple vehicles for businesses or organizations.",
        "price": 12.50,
    },
    3: {
        "title": "Basic Vacuuming",
        "description": "Cleaning the interior carpets and seats with a vacuum.",
        "price": 15.00,
    },
    4: {
        "title": "Windows Cleaning",
        "description": "Streak-free cleaning of interior and exterior glass surfaces.",
        "price": 12.00,
    },
    5: {
        "title": "Tire and Wheel Cleaning",
        "description": "Cleaning and shining tires, rims, and hubcaps.",
        "price": 20.00,
    },
    6: {
        "title": "Full Interior Detailing",
        "description": "Deep cleaning of upholstery, carpets, dashboard, and vents.",
        "price": 100.00,
    },
    7: {
        "title": "Exterior Waxing and Polishing",
        "description": "Adding a protective shine to the car’s paint.",
        "price": 75.00,
    },
    8: {
        "title": "Clay Bar Treatment",
        "description": "Removing contaminants from the car’s surface.",
        "price": 50.00,
    },
    9: {
        "title": "Engine Bay Cleaning",
        "description": "Degreasing and cleaning the engine compartment.",
        "price": 40.00,
    },
    10: {
        "title": "Paint Restoration",
        "description": "Buffing and polishing to restore paint finish.",
        "price": 150.00,
    },
    11: {
        "title": "Scratch and Swirl Removal",
        "description": "Repairing minor paint damage.",
        "price": 75.00,
    },
    12: {
        "title": "Odor Removal",
        "description": "Eliminating smells with ozone treatments or specialized sprays.",
        "price": 30.00,
    },
    13: {
        "title": "Pet Hair Removal",
        "description": "Specialized cleaning for pet hair in the interior.",
        "price": 25.00,
    },
    14: {
        "title": "Rain Repellent Application",
        "description": "Treating windshields to improve visibility in rain.",
        "price": 20.00,
    },
    15: {
        "title": "Underbody Wash",
        "description": "Removing dirt and grime from the underside of the car.",
        "price": 25.00,
    },
}

def fleet_car_cost(cars):
    """Calculate the fleet washing cost based on the number of cars."""
    base_price = 12.5
    total_price = 0

    for i in range(0, cars, 5):  # Process in chunks of 5 cars
        chunk_size = min(5, cars - i)  # Handle the last chunk if it's less than 5
        discount = (i // 5) * 0.5  # $0.50 discount for every group of 5 cars
        price_per_car = base_price - discount
        total_price += chunk_size * price_per_car

    # Update the Fleet Washing price in the dictionary
    car_wash_services[2]["price"] = total_price

    print(f"Total price for {cars} cars: ${total_price:.2f}")
    print(f"Price per car: ${total_price / cars:.2f}")

def main():
    print("Car wash cost calculator")
    cars = int(input("Enter the number of cars you want to wash: "))
    fleet_car_cost(cars)

    if cars == 1:
        payment.append({
            "title": car_wash_services[1]["title"],
            "price": car_wash_services[1]["price"]
        })
    elif 5 >= cars > 1:
        payment.append({
            "title": car_wash_services[1]["title"],
            "price": car_wash_services[1]["price"] * cars
        })
    else:
        to_fleet_or_not_to_fleet = input(
            "You are eligible for fleet washing services. Would you like to go with this option, or continue with the regular car wash? (Fleet/Regular): "
        ).capitalize()

        if to_fleet_or_not_to_fleet == "Fleet":
            payment.append({
                "title": car_wash_services[2]["title"],
                "price": car_wash_services[2]["price"]
            })
        else:
            payment.append({
                "title": car_wash_services[1]["title"],
                "price": car_wash_services[1]["price"] * cars
            })

    print("Here are the other services we provide:")
    print(service_titles)

    while True:
        service_determinator = input(
            "Are there any services you would like to add, learn more about, or just skip? (Add/Learn/Skip): "
        ).capitalize()

        if service_determinator == "Add":
            add_service = int(input("Enter the number of the service you would like to add: "))
            if add_service in car_wash_services:
                payment.append({
                    "title": car_wash_services[add_service]["title"],
                    "price": car_wash_services[add_service]["price"]
                })
                print(f"Added {car_wash_services[add_service]['title']} to the payment list.")
            else:
                print("Invalid service number. Please try again.")

        elif service_determinator == "Learn":
            learn_service = int(input("Enter the number of the service you would like to learn more about: "))
            if learn_service in car_wash_services:
                print(car_wash_services[learn_service]["description"])
            else:
                print("Invalid service number. Please try again.")

        elif service_determinator == "Skip":
            print("Skipping to the next action.")
            break  # Exit the loop when 'Skip' is selected

        else:
            print("Invalid option. Please choose 'Add', 'Learn', or 'Skip'.")

    print("This is the current list of services you have selected:")
    print(payment)
    final_test = input("Is this what you selected? (Yes/No): ").capitalize()

    if final_test == "Yes":
        print("Thank you for using our service. Calculating the total cost now.")
    else:
        print("Please try again.")
        exit()

    price = [service['price'] for service in payment]
    total_price = sum(price)

    if to_fleet_or_not_to_fleet == "Fleet":
        total_cost = cars * total_price - ((cars - 1) * car_wash_services[2]["price"])
    else:
        total_cost = total_price * cars

    print(f"The total cost of washing {cars} cars is ${total_cost:.2f}")
    print("Thank you for using our service")

if __name__ == "__main__":
    main()
