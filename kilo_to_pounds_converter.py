# Converter function
def kg_to_pounds(kg):
    if kg < 0:
        raise ValueError("Weight cannot be negative.")
    return kg * 2.20462

# Main function
def main():
    # Get the weight in kg
    kg = float(input("Enter weight in kg: "))
    # Convert the weight to pounds
    pounds = kg_to_pounds(kg)
    # Print the weight in pounds
    print(f"Weight in pounds: {pounds:.3f}")

# Call the main function
if __name__ == "__main__":
    main()