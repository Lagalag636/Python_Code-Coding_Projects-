def character_to_be_counted():
    character = input("Enter a character you want to count in a word: ")
    return character

def word_with_character(character):
    word = input("Enter the word(s) you want to count the character in: ")
    return word

def counting_the_character(character, word):
    count = 0
    for i in word:
        if i == character:
            count += 1
    return count

if __name__ == "__main__":
    print("We are going to count the number of times a character appears in a word.")
    character = character_to_be_counted()
    word = word_with_character(character)
    count = counting_the_character(character, word)
    print(f"{character} appears {count} times in {word}.")