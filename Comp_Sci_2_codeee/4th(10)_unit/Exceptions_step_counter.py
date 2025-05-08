def steps_to_miles(user_steps):
    miles = user_steps / 2000
    return round(miles, 2)

if __name__ == '__main__':
    try:
        user_steps = float(input("Enter the number of steps: "))
        if user_steps < 0:
            raise ValueError("Negative step count entered.")  # Raise an exception for negative input
        print("You have walked", steps_to_miles(user_steps), "miles.")
    except ValueError as e:
        print(f"Exception: {e}")

