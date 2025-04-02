# Read coefficients for the first equation: ax + by = c
a = int(input("Enter a (coefficient of x in first equation): "))
b = int(input("Enter b (coefficient of y in first equation): "))
c = int(input("Enter c (constant in first equation): "))

# Read coefficients for the second equation: dx + ey = f
d = int(input("Enter d (coefficient of x in second equation): "))
e = int(input("Enter e (coefficient of y in second equation): "))
f = int(input("Enter f (constant in second equation): "))

# Loop through possible values of x and calculate corresponding y
solution_found = False
for x in range(-10, 11): # Checking x values from -10 to 10
    if b != 0: # Avoid division by zero
        y1 = (c - a * x) / b # Solve for y using the first equation
    # Check if this y satisfies the second equation
    if d * x + e * y1 == f:
        print(f"Solution found: x = {x:.2f}, y = {y1:.2f}")
        solution_found = True
# If no solution was found
if not solution_found:
 print("No solution found in the given range.")
