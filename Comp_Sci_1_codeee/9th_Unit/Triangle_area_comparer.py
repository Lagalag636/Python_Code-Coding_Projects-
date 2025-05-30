class Triangle:   
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle_base1 = float(input("Enter the base for triangle 1: "))
    triangle_height1 = float(input("Enter the height for triangle 1: "))
    triangle_base2 = float(input("Enter the base for triangle 2: "))
    triangle_height2 = float(input("Enter the height for triangle 2: "))
    triangle1 = Triangle(triangle_base1, triangle_height1)
    triangle2 = Triangle(triangle_base2, triangle_height2)

    # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
      
    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    print('Triangle with smaller area:')  # Output header
    if triangle1.get_area() > triangle2.get_area():
        triangle2.print_info()
    else:
        triangle1.print_info()
    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())

