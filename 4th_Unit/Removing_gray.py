num1 = int(input("Please input the number for red: "))
num2 = int(input("Please input the number for green: "))
num3 = int(input("Please input the number for blue: "))

# Check if any input is greater than 255
if num1 > 255 or num2 > 255 or num3 > 255:
    print("One of your inputs is not valid. Any number over 255 is not an RGB color.")
else:
    # Find the smallest number
    smallest_num = min(num1, num2, num3)

    # Subtract the smallest number from all inputs
    num1 -= smallest_num
    num2 -= smallest_num
    num3 -= smallest_num

    print(f"Here is your color without the gray: {num1, num2, num3}")
