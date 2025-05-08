#import unittest
def intro(): 
    print("This is the Fibonacci sequence model.")
    print("This model will generate the Fibonacci sequence to the number you specify.")

def fibonacci(n, memo={}):
    # Check if result is already in the memo
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Store the result in the memo before returning it
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]



if __name__ == '__main__':
    intro()
    start_num = int(input("Enter which number you would like to find in the fibonacci sequence: "))
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')