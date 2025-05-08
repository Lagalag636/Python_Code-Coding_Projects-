from datetime import date, timedelta, time

# 1 Complete read_date()
def read_date():
    """Read a string representing a date in the format 2121-04-12, create a
    date object from the input string, and return the date object
    """
    date_str = input("Enter a date in the format YYYY-MM-DD: ")
    year, month, day = map(int, date_str.split('-'))
    return date(year, month, day)

# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list

if __name__ == '__main__':
    print("Date Translation")
    num_of_dates = int(input("How many dates would you like to enter? "))
    date_list = []
    
    for i in range(num_of_dates):
        func_date = read_date()
        date_list.append(func_date)

    for i in range(num_of_dates):
        print(f"Date {i+1}: {date_list[i]}")
    # 3. Use sorted() to sort the dates, earliest first

    sorted_dates = sorted(date_list)

# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy

    print("\nSorted Dates (mm/dd/yy):")
    for d in sorted_dates:
        print(d.strftime("%m/%d/%y"))

# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number

    if len(sorted_dates) >= 2:
        days_between = abs((sorted_dates[-1] - sorted_dates[-2]).days)
        print(f"\nDays between the last two dates: {days_between} days")
    else:
        print("\nNot enough dates to calculate the difference.\nA.K.A. ya screwed up")

    # 6. Output the date that is 3 weeks from the most recent date in the list

    most_recent_date = sorted_dates[-1]  # Last element in sorted list
    future_date = most_recent_date + timedelta(weeks=3)
    print(f"\nDate 3 weeks from the most recent date: {future_date.strftime('%Y-%m-%d')}")

    # 7. Output the full name of the day of the week of the earliest day
    earliest_date = sorted_dates[0]  # First element in sorted list
    print(f"\nThe earliest date falls on a {earliest_date.strftime('%A')}")
