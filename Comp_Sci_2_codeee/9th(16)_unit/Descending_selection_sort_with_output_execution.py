def selection_sort_descending(input_array):
    array_length = len(input_array)
    min_value = min(input_array)  # Find the minimum value in the array
    min_index = input_array.index(min(input_array))  # Get index of the minimum value
    input_array[-1], input_array[min_index] = input_array[min_index], input_array[-1] #swap the minimum value with the last element
    min_index = input_array.index(min(input_array))  # Get index of the minimum value
    for primary_number in range(array_length):
        # Assume the first unsorted element is the largest
        max_index = primary_number
        for secondary_number in range(primary_number + 1, array_length):
            if input_array[secondary_number] > input_array[max_index]:
                max_index = secondary_number
                print("I have found a new maximum value:", input_array[max_index])
                print(f"Step {primary_number + 1}: {input_array}")
            elif max_index == min_index:
                return input_array 
        # Swap the found maximum element with the first unsorted element
        input_array[primary_number], input_array[max_index] = input_array[max_index], input_array[primary_number]
        

if __name__ == "__main__":
    list_to_sort = [int(inputted_integer) for inputted_integer in input("Enter numbers separated by spaces: ").split()]
    selection_sort_descending(list_to_sort)
    print("Test list sorted in descending order:", list_to_sort)
