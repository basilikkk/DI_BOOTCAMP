
import random

# Step 1:
user_input = input("Please enter a string (10 characters long): ")

# Step 2: 
if len(user_input) < 10:
    print("string not long enough")
elif len(user_input) > 10:
    print("string too long")
else:
    print("perfect string")

    # Step 3: 
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")
    
    # Step 4: 
    constructed_string = ""
    for char in user_input:
        constructed_string += char
        print(constructed_string)

    # Bonus Step: 
    user_input_list = list(user_input)
    random.shuffle(user_input_list)
    jumbled_string = ''.join(user_input_list)
    print(f"Jumbled string: {jumbled_string}")
