my_fruit1 = input("Please enter a fruit: ")
my_fruit2 = input("Please enter another fruit: ")
my_fruit3 = input("Please keep entering fruit: ")

your_fruit1 = input("Please keep feeding- *ahem* entering fruit: ")
your_fruit2 = input("Please enter just one more fruit: ")

their_fruit = input("Please enter one more and I'll be full: ")
print("Thanks")

def kill_repititions():
    for item in fruit_list:
        if item not in clean_fruit_list:
            clean_fruit_list.append(item)
    return clean_fruit_list

fruit_list = [my_fruit1, my_fruit2, my_fruit3]
clean_fruit_list = []
kill_repititions()
print(sorted(clean_fruit_list))

fruit_list.append(your_fruit1)
fruit_list.append(your_fruit2)
kill_repititions()
print(sorted(clean_fruit_list))

fruit_list.append(their_fruit)
kill_repititions()
print(sorted(clean_fruit_list))

fruit_list.append(your_fruit1)
kill_repititions()
print(sorted(clean_fruit_list))

kill_repititions()
clean_fruit_list.remove('apple')
print(sorted(clean_fruit_list))