class SimpleCar:
    def __init__(self, miles):
        self.miles = miles

    def drive(self, dist):
        dist = int(input("how far do you want the car to drive?"))
        self.miles = self.miles + dist
        print(f"you have driven {dist}. you are at {self.miles}")
       
    def reverse(self, dist):
        dist = int(input("how far do you want the car to reverse?"))
        self.miles = self.miles - dist
        print(f"you have reversed {dist}. you are at {self.miles}")
       
    def get_odometer(self):
        return self.miles
   
    def honk_horn(self):
        print('beep beep')
       
    def report(self):
        print(f'Car has driven: {self.miles} miles')
       
if __name__ == "__main__":
    run = True
    Mike = SimpleCar(0)
    while run == True:
        print("choose one of these three things that Mike can do\n 1. Mike can drive forward.\n 2. Mike can reverse.\n 3. Mike can honk.\n 4. Exit program")
        user_input = int(input(""))
        dist = 0
        if user_input == 1:
            Mike.drive(dist)
        elif user_input == 2:
            Mike.reverse(dist)
        elif user_input == 3:
            Mike.honk_horn()
        else:
            run = False
    
    print(Mike.report())