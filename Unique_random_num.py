import random

def unique_random_ints(amount_of_int, max_int, user_seed):
    """Return a list of unique randomly generated numbers from 0 to max_int (inclusive).
    Track the number of retries due to exceeding max_int and due to duplicates.
    """
    random.seed(user_seed)  # Set seed for reproducibility
    nums = set()  # Using a set to ensure uniqueness
    retry_count_exceed = 0  # Tracks numbers that exceed max_int
    retry_count_duplicate = 0  # Tracks duplicate numbers

    while len(nums) < amount_of_int:
        rand_num = random.randint(0, max_int)  # Generate a number
        
        if rand_num > max_int:  # Should never happen since randint(0, max_int) is always valid
            retry_count_exceed += 1
            print(f"Generated {rand_num}, which exceeds {max_int}. Retrying...")
        elif rand_num in nums:  # If the number is already in the set, count as duplicate retry
            retry_count_duplicate += 1
            print(f"Generated {rand_num}, which is a duplicate. Retrying...")
        else:
            nums.add(rand_num)  # Add only unique, valid numbers

    print(f"\nTotal retries due to exceeding max_int: {retry_count_exceed}")
    print(f"Total retries due to duplicates: {retry_count_duplicate}")

    return list(nums), retry_count_duplicate + retry_count_exceed  # Convert set to list before returning

if __name__ == '__main__':
    user_seed = int(input("What seed would you like to use? "))
    amount_of_int = int(input("How many numbers would you like to generate? "))
    max_int = int(input("What is the maximum number to not exceed? "))

    random_numbers, retries = unique_random_ints(amount_of_int, max_int, user_seed)
    print("\nGenerated numbers:", random_numbers, "; retries:", retries)
