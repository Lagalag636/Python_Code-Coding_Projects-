f0 = 10
r = 2
frequencies = [f0 * pow(r, exponent) for exponent in range(4)]
#print(f"{frequencies}")
#for item in frequencies:
    #print(f"our item in the list is: {item}")
our_frequency = []
print(f"this is our new list: {our_frequency} which should be an empty list")

def append_items(our_frequency, current_frequency):
    our_frequency.append("duck")
    our_frequency.append(current_frequency)
    our_frequency.append("Bob")

for index in range(4):
    print(f"index is: {index}")
    print(f"this is our current list before appending our current frequency: {our_frequency}")

    current_frequency = f0 * pow(r, index)
    print(f"our current frequency is: {current_frequency}")
    append_items(our_frequency, current_frequency)
    print(f"this is our current list after appending our current frequency: {our_frequency}")
    our_frequency_postion_in_the_list = 3 * index + 1
    print(f"for index {index} our list position we want is {our_frequency_postion_in_the_list}")
    print(f"for index {index} our frequency from the list is {our_frequency[our_frequency_postion_in_the_list]}")


for index in range(4):
    our_frequency_postion_in_the_list = 3 * index + 1
    print(f"for index {index} our frequency from the list is {our_frequency[our_frequency_postion_in_the_list]}")

for item in our_frequency:
    if isinstance(item, int):  # Check if the item is an integer
        print(f"Our frequency is: {item}")

print('do it again')
clean_freq_list =[]
for item in our_frequency:
    
    token_as_string = str(item)
    print(f'our token as a string is: {token_as_string}')
    if token_as_string.isnumeric():
        clean_freq_list.append(item)
        
print(f"{clean_freq_list}")

