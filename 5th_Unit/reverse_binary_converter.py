binary_num = int(input("Enter a number: "))
if binary_num < 0:
    print("Please enter a positive number")
    exit()

binary_num_list = []

while binary_num > 0:
    binary_num_list.append(binary_num % 2)
    binary_num = binary_num // 2

print(f"This is your number in reverse binary! {binary_num_list}")
