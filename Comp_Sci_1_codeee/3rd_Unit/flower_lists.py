my_flower1 = input("Please input a flower: ")
my_flower2 = input("Please input another flower: ")
my_flower3 = input("Please input a different flower: ")
print(f"These are your flowers: {my_flower1, my_flower2, my_flower3}")
your_flower1 = input("Please ask a friend their favorite flower: ")
your_flower2 = input("Please ask a different friend their favorite flower: ")

their_flower = input("Please collectively decide on a favorite flower: ")

my_list = [my_flower1, my_flower2, my_flower3]
print(f"Here is my flower list: {my_list}")

your_list = [your_flower1, your_flower2]
print(f"Here is your friend's list of flowers: {your_list}")

my_list.extend(your_list)
our_list = my_list
print(our_list)

our_list.append(their_flower)
print(our_list)

our_list.remove(my_flower2)
our_list.insert(1, their_flower)
print(our_list)

our_list.remove(their_flower)
print(our_list)

our_list.pop(1)
print(our_list)

string_to_int = {
    'daisy': 1,
    'daphodile': 2,
    'tulip': 3
}

def convert_string_to_int(s):
    return string_to_int.get(s, 'Unknown string')

# Example calls
#print(convert_string_to_int('apple'))  # Output: 1 (because 'apple' is a key in the dictionary)
#print(convert_string_to_int('daisy'))  # Output: 'Unknown string' (because 'daisy' is not a key in the dictionary)
