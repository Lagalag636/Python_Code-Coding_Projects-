def get_valid_input(prompt, length=3):
    while True:
        user_input = input(prompt)
        if len(user_input) == length:
            return user_input
        else:
            print(f"Invalid input. Please enter exactly {length} characters.")

base_char = get_valid_input("Please enter three characters: ")
head_char = get_valid_input("Please enter a different three characters: ")


shaft = base_char *6
row1 = '      ' *3 + head_char
row2 = shaft + head_char *2
row3 = shaft + head_char *3
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

