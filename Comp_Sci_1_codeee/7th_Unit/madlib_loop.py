import random
def get_first_word():
    return input("Enter your first noun:")

def get_second_word():
    return input("Enter your second noun:")

def get_third_word():
    return input("Enter your third noun:")

def get_madlib():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return f"The {first_word} hid from the {second_word} and because {third_word} was with them."
    elif random_number == 2:
        return f"The {first_word} ran around the {second_word} and discovered the {third_word}."
    else:
        return f"The {first_word} flew over the {second_word} after being thrown by the {third_word}."




if __name__ == '__main__':
    while True:
        print("We will construct a madlib together.")
        first_word = get_first_word()
        second_word = get_second_word()
        third_word = get_third_word()
        madlib = get_madlib()
        print(madlib)
        play_again = input("Would you like to play again? (yes/no)")
        if play_again != "yes":
            print("Goodbye! Have a good day!")
            break