import random
import time
seed = time.time()
def get_int_data():
    int_data_list = [random.randint(0, 200) for _ in range(15)]
    return int_data_list

def user_data_input_decision():
    user_input = input("Would you like to enter your own data? (y/n): ").lower()
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return user_data_input_decision()
    
def get_user_range():
    user_range = input("Enter the range you would like to find(lower# - higher#): ")
    if user_range.count('-') == 1:
        lower_bound, upper_bound = map(int, user_range.split('-'))
    elif user_range.count(' - ') == 1:
        lower_bound, upper_bound = map(int, user_range.split(' - '))
    else:
        print("Invalid range format. Please enter in the format 'lower# - higher#'.")
        return get_user_range()
    return lower_bound, upper_bound

def intro():
    print("This program will find the range of numbers in a list.")
    print("You can either enter your own data or use the default data.")

if __name__ == '__main__':
    intro()
    decision = user_data_input_decision()
    if decision == True:
        user_data = input("Please enter a list of integers separated by spaces: ")
        int_data_list = [int(x) for x in user_data.split()]
        print(f"Your data is: {int_data_list}")
    else:
        int_data_list = get_int_data()
        print(f"Your data is: {int_data_list}")
    lower_bound, upper_bound = get_user_range()
    numbers_in_range = [num for num in int_data_list if lower_bound <= num <= upper_bound]

    if numbers_in_range:
        print(f"Numbers within the range {lower_bound}-{upper_bound}: {numbers_in_range}")
    else:
        print(f"No numbers found within the range {lower_bound}-{upper_bound}.")
