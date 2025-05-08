class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, purchased_bottles):
        self.bottles = self.bottles - purchased_bottles
      
    def restock(self, restocked_bottles):
        self.bottles = self.bottles + restocked_bottles
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    vending_machine = VendingMachine()
    # TODO: Purchase input number of drinks
    print("This is a vending machine!")
    purchased_bottles = int(input("How many bottles do you want to purchase? "))
    vending_machine.purchase(purchased_bottles)
    # TODO: Restock input number of bottles
    restocked_bottles = int(input("How many bottles do you want to restock? "))
    vending_machine.restock(restocked_bottles)
    # TODO: Report inventory
    vending_machine.report()