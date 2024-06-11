""""A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


How much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).
"""

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost=0
for key, value in family.items():
    if value > 12:
        total_cost+=15
    elif  3<=value<=12:
        total_cost+=10
    elif value < 3:
        pass   
print(total_cost)        

#bonus
number_new_family=int(input('please enter a number of people of your family'))
names=[]
ages=[]
for i in range(number_new_family):
    name=input('enter a name ')
    names.append(name)
    age=int(input('enter a age '))
    ages.append(age)

new_family=dict(zip(names,ages))  

total_cost_new=0
for key, value in new_family.items():
    if value > 12:
        total_cost_new+=15
    elif  3<=value<=12:
        total_cost_new+=10
    elif value < 3:
        pass   
print(total_cost_new)    
