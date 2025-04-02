class FoodItem:
    # Constructor to initialize name, fat, carbs, and protein attributes
    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
       
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')

if __name__ == "__main__":
    item_name = input("What is the name of the food item? ")
    
    if item_name.lower() == 'water':
        # Water is assumed to have 0 fat, carbs, and protein
        food_item = FoodItem(item_name, 0.0, 0.0, 0.0)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
    else:
        amount_fat = float(input(f"How many grams of fat does the {item_name} have? "))
        amount_carbs = float(input(f"How many grams of carbs does the {item_name} have? "))
        amount_protein = float(input(f"How many grams of protein does the {item_name} have? "))
        num_servings = float(input(f"How many servings would you like to calculate the calories for? "))
        
        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')
'''M&M's
10.0
34.0
2.0
3.0
sloppy joe
'''