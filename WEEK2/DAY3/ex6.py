from datetime import datetime

def minutes_lived(birthdate_str):
    # Define the format of the input birthdate string
    birthdate_format = "%Y-%m-%d"  # Example format: 'YYYY-MM-DD'
    
    # Parse the input birthdate string into a datetime object
    birthdate = datetime.strptime(birthdate_str, birthdate_format)
    
    # Get the current date and time
    now = datetime.now()
    
    # Calculate the time difference between now and the birthdate
    time_difference = now - birthdate
    
    # Convert the time difference to minutes
    minutes_lived = time_difference.total_seconds() / 60
    
    # Display the result
    print(f"You have lived for {int(minutes_lived)} minutes.")

# Example usage
birthdate_input = "2000-04-21"  # Replace with the actual birthdate
minutes_lived(birthdate_input)
