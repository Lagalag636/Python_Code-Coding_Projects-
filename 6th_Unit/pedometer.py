# Define your function here 
def feet_to_steps(steps, distance):
    # Calculate the average step length
    step_length = distance / steps
    return step_length

def steps_to_integer(step_length):
    step_length= int(step_length)
    return step_length 

if __name__ == '__main__':
    distance = float(input("How many feet did you walk today? "))
    steps = 2.5
    step_length = feet_to_steps(steps, distance)
    step_length = steps_to_integer(step_length)
    print("The steps you walked today is: ", step_length)