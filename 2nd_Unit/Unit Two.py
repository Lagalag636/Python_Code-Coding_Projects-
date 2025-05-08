def division_of_integers(user_num, div_num):

    if div_num == 0:
        print("Error: Division by zero is not allowed. ")
        return

    result1 = user_num // div_num
    result2 = result1 // div_num
    result3 = result2 // div_num

    print(f"Result after first division: {result1} \nResult after second division: {result2} \nResult after third division: {result3}")

def get_user_input():
    #TODO put this inside a while loop and don't let the user move on until they get it right
    user_num = int(input("Enter your first integer: "))
    div_num = int(input("Enter your second integer: "))
    return user_num, div_num

user_num, div_num = get_user_input()

division_of_integers(user_num, div_num)

#import math

#dividend = input("Please input a number you would like to know the square root of: ")

#try:
    #dividend = float(dividend)
#except ValueError:
    #print("The value must be a number.")
    #dividend = None

#if dividend is not None:
    #sqrt_process = math.sqrt(dividend)
    #quotient = sqrt_process
    #print(f"Square root of {dividend:.2f} = {quotient:.2f}")
#else: print("Could not compute the float")

#two = 2
#f0 = input("Please give a frequency:")
#f0 = float(f0)
#r = pow(two, 1/12)
#n = 1
#rn = pow(r, n)
#first_equation = (f0*rn)
#n = 2
#rn = pow(r, n)
#second_equation = (f0*rn)
#n = 3
#rn = pow(r, n)
#third_equation = (f0*rn)
#print(f"{f0} Hz \n{first_equation:.2f} Hz \n{second_equation:.2f} Hz \n{third_equation:.2f} Hz")

#condensed version of code above:

# Define the base frequency ratio for equal temperament tuning
r = pow(2, 1/12)

# Get user input for the base frequency and convert it to a float
f0 = float(input("Please give a frequency: "))

# List to hold the frequencies
frequencies = [f0 * pow(r, n) for n in range(4)]  # Including f0 itself and the next 3 semitones

# Print the results
print("\n".join(f"{freq:.2f} Hz" for freq in frequencies))
