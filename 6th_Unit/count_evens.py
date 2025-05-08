def count_evens(num1, num2, num3, num4, num5):
    count = 0
    if num1 % 2 == 0:
        count += 1
    if num2 % 2 == 0:
        count += 1
    if num3 % 2 == 0:
        count += 1
    if num4 % 2 == 0:
        count += 1
    if num5 % 2 == 0:
        count += 1
    return count



if __name__ == '__main__':
    print("Please enter five numbers: ")
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    num3 = int(input("Third number: "))
    num4 = int(input("Fourth number: "))
    num5 = int(input("Fifth number: "))
   
    result = count_evens(num1, num2, num3, num4, num5)
    print(f'The total even numbers you inputted are: { result }')
