from datetime import datetime, timedelta

def time_until_new_year():
    # Get the current date and time
    now = datetime.now()
    
    # Calculate the next January 1st
    current_year = now.year
    next_year = current_year + 1
    new_year = datetime(year=next_year, month=1, day=1)
    
    # Calculate the time difference
    time_difference = new_year - now
    
    # Extract days, hours, minutes, and seconds from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Format the result
    result = f"The 1st of January is in {days} days, {hours:02}:{minutes:02}:{seconds:02} hours."
    print(result)

# Example usage
time_until_new_year()
