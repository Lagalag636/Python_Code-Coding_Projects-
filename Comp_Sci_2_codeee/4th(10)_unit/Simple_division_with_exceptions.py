if __name__ == "__main__":
    
    try:
        user_number = int(input("Enter a whole number: "))
        div_number = int(input("Enter a whole number to divide by: "))
        print(user_number / div_number)
    except ValueError as e:
        print(f"Input exception: {e}")
    except ZeroDivisionError as e:
        print(f"Zero Division Exception: integer division or modulo by zero.")
    