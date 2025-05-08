def primary_high(road_num):
    road_num_int = int(road_num)
    if road_num_int == 0 or road_num_int % 100 == 0:
        return f"{road_num} is not a valid interstate highway number."
    elif road_num_int % 2 == 0:
        return f"I-{road_num} is primary, going east/west."
    else:
        return f"I-{road_num} is primary, going north/south."
    
def auxiliary_high(road_num):
    road_num_int = int(road_num)
    if road_num_int == 0 or road_num_int % 100 == 0:
        return f"{road_num} is not a valid interstate highway number."
    else:
        serving_num = road_num_int % 100
        if serving_num % 2 == 0:
            return f"I-{road_num} is an auxiliary highway, serving I-{serving_num}, going east/west."
        else:
            return f"I-{road_num} is an auxiliary highway, serving I-{serving_num}, going north/south."


def check_length_num(road_num):
    if len(road_num) > 3 or len(road_num) < 1:
        return f"{road_num} is not a valid interstate highway number."
    elif len(road_num) <= 2:
        return primary_high(road_num)
    else:
        return auxiliary_high(road_num)

road_num = (input("Please enter a series of digits to see if it is a Highway: "))
result = check_length_num(road_num)
print(result)





def check_odd_even(road_num):
    if road_num == 0 or 200:
        return print(f"{road_num} is not a valid interstate highway number.")
    if road_num % 2 == 0:
        return print(f"I-{road_num} is a interstate highway that runs east/west.")
    else:
        return "Odd north/south."

#print(f"I-{road_num} is a highway that runs from ")