base_char = input("Please enter a character: ")
head_char = input("Please enter a different character: ")

# Define the space variable for formatting
space = ' '

# Function to print a pattern based on base_char and head_char
def print_pattern(base_char, head_char, spaces):
    shaft = base_char * 6
    row1 = spaces + head_char
    row2 = shaft + head_char * 2
    row3 = shaft + head_char * 3
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

# Determine how many spaces to use
if base_char <= head_char:
    if len(base_char) == 1 and len(head_char) == 1:
        space_count = len(base_char)  # Count of spaces
        if space_count in [1, 2, 3, 4, 5, 6]:
            spaces = space * (space_count * 3)
            print_pattern(base_char, head_char, spaces)
        else:
            print("Sorry, but the first character must be smaller or equal to the second.")
    else:
        print("Sorry, invalid input. Please ensure both characters are single characters.")
else:
    print("Sorry, but the first character must be smaller or equal to the second.")
