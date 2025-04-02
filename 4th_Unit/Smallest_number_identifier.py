#integer_set = []

#for index in range(3):
    #grab_num = int(input("Please put in an integer: "))
    #integer_set.append(grab_num)

#integer_set.sort
#print(integer_set)
#if integer_set[0] >= integer_set[1]:
    #offset_num = integer_set.pop(0)
    #integer_set.insert(1, offset_num)
#else:
    #print(integer_set)

#print(f"This is the smallest integer you inputted: {integer_set[2]}")


num1 = int(input("Please input an integer: "))
num2 = int(input("Please input an integer: "))
num3 = int(input("Please input an integer: "))
if num1 >= num2 and num2 >= num3:
    print(f"The smallest integer you inputted is {num3}")
elif num2 >= num1 and num1 >= num3:
    print(f"The smallest integer you inputted is {num3}")
elif num3 >= num1 and num1 >= num2:
    print(f"The smallest integer you inputted is {num2}")
elif num1 >= num3 and num3 >= num2:
    print(f"The smallest integer you inputted is {num2}")
else:
    print(f"The smallest integer you inputted is {num1}")
