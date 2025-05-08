def find_factors_recursive(number, current=1, factors=None):
    if factors is None:
        factors = []

    if current > number:
        return factors

    if number % current == 0:
        factors.append(current)

    return find_factors_recursive(number, current + 1, factors)

if __name__ == "__main__":
    print("I am somewhat working...")

# Get input from the user
    num = int(input("Enter a number under 997: "))

# Find and print factors
    factors = find_factors_recursive(num)
    print(f"The factors of {num} are: {factors}")
