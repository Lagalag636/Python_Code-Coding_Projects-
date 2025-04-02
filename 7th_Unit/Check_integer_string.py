def get_user_input():
    user_input = input("Enter a string: ")
    return user_input

def test_integer_string(user_input):
    if user_input.isdigit():
        return print("Yes, your input is an integer string.")
    else:
        return print("No, your input is not an integer string.")

if __name__ == '__main__':
    print("We are determining if your input is an integer string or not.")
    user_input = get_user_input()
    test_integer_string(user_input)
    