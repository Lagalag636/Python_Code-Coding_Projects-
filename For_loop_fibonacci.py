def fibonacci(n):
    """
    Generate the first n numbers of the Fibonacci sequence.
    :param n: Number of terms to generate
    :return: A list containing the Fibonacci sequence
    """
    if n < 0:
        raise ValueError("Weight cannot be negative.") # Return an error for invalid input
    elif n == 0:
        return [0]  # Return the first Fibonacci number
    elif n == 1:
        return [1]  # Return the first Fibonacci number
    
    # Start the sequence with the first two numbers
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        # Add the last two numbers in the list to get the next number
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

if __name__ == "__main__":
    n = int(input("Enter the number of terms to generate: "))
    sequence = fibonacci(n)
    print(sequence)