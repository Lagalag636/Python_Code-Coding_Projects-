def get_user_input():
    user_input = input()
    return user_input

def remove_non_alpha(user_input):
    clean_string = ''
    for i in user_input:
        if i.isalpha():
            clean_string += i
    print(clean_string)
    return clean_string

if __name__ == '__main__':
    print("Please enter a string you would like to remove non-alpha characters from: ")
    user_input = get_user_input()
    clean_string = remove_non_alpha(user_input)
    print("Is the cleaned string to your liking?")
    pleased_factor = input("Yes or No:")
    pleased_factor = pleased_factor.lower()
    if pleased_factor == "yes":
        print("Great! Have a good day!")
    else:
        print("I'm sorry to hear that.")