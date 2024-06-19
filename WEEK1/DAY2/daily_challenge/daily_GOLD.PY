from datetime import datetime
current_date=datetime.today()
print(current_date)


def calculate_age(birthdate):
    today=datetime.today()
    age=today.year - birthdate.year
    if today.month< birthdate.month or(today.month==birthdate.month and today.day> birthdate.day):
        age-=1
    return age 
def create_cake(num_i):
    total_width = 11  # Width for the 'i' characters and spaces
    i_chars = 'i' * (num_i%10)
    spaces_each_side = (total_width - num_i) // 2  # Calculate spaces needed on each side

    # Create the top part with centered 'i' characters
    top_part = f"{' ' * spaces_each_side}{i_chars}{' ' * spaces_each_side}"
    
    cake = f"""      ___{top_part}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~)"""
  

    print(cake) 
def main():
    date_of_birthday_str=input("please enter your birthdate' yyyy-mm-dd ")
    date_of_birthday =datetime.strptime(date_of_birthday_str,"%Y-%m-%d")
    age=calculate_age(date_of_birthday)
    print(age)
    print(date_of_birthday)
    create_cake(age)
main()

