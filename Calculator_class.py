class Calculator:
    def __init__(self):
        self.value = 0

    def addition(self, num1):
        self.value += num1
    
    def subtraction(self, num):
        self.value -= num
    
    def multiplication(self, num):
        self.value *= num

    def division(self, num):
        self.value /= num

    def clear(self):
        self.value = 0

    def get_value(self):
        return self.value    
    # Type your code here.

if __name__ == "__main__":
    print("Welcome to the calculator!\nPlease help us test this calculator program by entering two numbers.")
    calc = Calculator()
    num1 = float(input("Add the first number to test the functions on this calculator: "))
    num2 = float(input("Add the second number to test the functions on this calculator: "))

    # 1. The initial value
    print(f'{calc.get_value():.1f}')

    # 2. The The value after adding num1
    calc.addition(num1)
    print(f'{calc.get_value():.1f}')

    # 3. The value after multiplying by 3
    calc.multiplication(3)
    print(f'{calc.get_value():.1f}')

    # 4. The value after subtracting num2
    calc.subtraction(num2)
    print(f'{calc.get_value():.1f}')

    # 5. The value after dividing by 2
    calc.division(2)
    print(f'{calc.get_value():.1f}')

    # 6. The value after calling the clear() method
    calc.clear()
    print(f'{calc.get_value():.1f}')
