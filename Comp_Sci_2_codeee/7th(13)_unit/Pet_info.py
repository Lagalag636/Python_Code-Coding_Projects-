class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self, name, age, breed):
        Pet.__init__(self, name, age)
        self.breed = breed

    def print_info(self):
        Pet.print_info(self)
        print(f'   Breed: {my_cat.breed}')


if __name__ == "__main__":
    pet_name = input("What is the pet's name? ")
    pet_age = int(input("What is the pet's age? "))
    cat_name = input("What is your cat's name? ")
    cat_age = int(input("How old is your cat? "))
    cat_breed = input("What is your cat's breed? ")

    my_pet = Pet(pet_name, pet_age)
    my_cat = Cat(cat_name, cat_age, cat_breed)

    my_pet.print_info()
    my_cat.print_info()



# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()

# TODO: Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()

# TODO: Use my_cat.breed to output the breed of the cat
