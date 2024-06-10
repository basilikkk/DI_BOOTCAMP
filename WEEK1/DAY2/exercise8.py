"""Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping)."""
pizza_base_price=10
toppings=[]
topping=''
while topping != 'quit':
    topping=''
    topping=input('enter a pizza topping ')
    if topping != 'quit':
        print('you’ll add that topping to their pizza ')
        toppings.append(topping)
print(f'your toppings are {toppings}')    

sum=0
for i in toppings:
    sum+=2.5

final_price=sum+pizza_base_price

print(f"yout final price is {final_price}")