"""A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list."""


#family
total_cost = 0
family_count = int(input("Enter the number of family members: "))

for i in range(family_count):
    age=int(input('please anter the age of person  '))
    if age > 12:
        total_cost+=15
    elif 3<=age<=12:
        total_cost+=10
    else:
        total_cost+=0

print(f"total cost is {total_cost}")

#teenagers
print('teenagers')
print()
total_cost_teenagers=0

teenagers = ['Emil', 'Paul', 'Basil', 'Mike']
allowed_teenagers=[]
for i in teenagers:
    age=int(input('please enter the age of person  '))
    if age >=21:
        total_cost_teenagers+=15
        allowed_teenagers.append(i)
    elif 16<age>21:
        total_cost+=0
        print('are not permitted to watch the movie')  
    else:
        total_cost+=0   
    


    
print(f"total cost for teenagers is {total_cost_teenagers}")
print(f"allowed teenagers are {allowed_teenagers}")
