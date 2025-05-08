from datetime import datetime

def time_func():
    timeList = []
    now = datetime.now()
    
    # Extracting the current day, month, year, and hour
    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    second = now.second
    microseconds = now.microsecond
    milliseconds = microseconds / 1000
    # Adding them to the list
    timeList.extend([day, month, year, hour, minute, second, milliseconds, microseconds])
    
    print(timeList)
    
    biggest = max(timeList)
    average = sum(timeList) / len(timeList)
    
    print(f"The biggest number is: {biggest}, and the average is {average}.")

time_func()
