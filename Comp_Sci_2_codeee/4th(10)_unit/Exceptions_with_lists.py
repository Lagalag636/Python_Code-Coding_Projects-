import random

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']

selected_names = random.sample(names, 2)

# Create a copy of the list with asterisks replacing selected names
hidden_names = names[:]
for i, name in enumerate(hidden_names):
    if name in selected_names:
        hidden_names[i] = '*' * len(name)

# Check if password is correct
correct_password = "secret123"  # Change this to any password you like




if __name__ == "__main__":
    try:
        print("Hidden names:", hidden_names)
        index = int(input("Enter an index to print the name: "))
        print(hidden_names[index])
        password = input("Enter password to unveil names: ")

        if password == correct_password:
            print("Access granted! Original names:", names)
        else:
            print("Incorrect password. Names remain hidden.")
    
    
    
    except IndexError as e:
        print(f"Exception! {e}")
        if index < 0:
            print(f"The closest name is: {names[0]}")
        else:
            print(f"The closest name is: {names[-1]}")