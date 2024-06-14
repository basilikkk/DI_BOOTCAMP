""""Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month."""
import random

def main():
    month=input("what's the month now? ")
    temperature = get_random_temp(month)
    print(month)
    get_random_temp(month.lower())
   
    print(f"The temperature right now is {round(temperature,3)} degrees Celsius.") 
    if temperature<0:
        print('Brrr, that’s freezing! Wear some extra layers today”')
    elif 0 <= temperature< 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16<=temperature<23:
        print('Nice weather for walking around')
    elif 23<=temperature<32:
        print("Let's go to the beach")
    elif 32<=temperature<=40:
        print("You'd better to stay home and stay hydrated")

        


def get_random_temp(month):
    if month==('june' or 'july' or 'august'):
        return (random.uniform(22,40))
    elif month==('december' or 'january' or 'february'):
         return (random.uniform(-10,16))
      
    elif month=='march' or month=='april' or month=='may':
        return (random.uniform(8,22))
    elif month=='september' or 'october' or 'november':
        return (random.uniform(5,18))
   


main()

        

