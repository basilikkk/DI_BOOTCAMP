"""Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers."""
import random

def comparison(a):
    b=random.randint(1,100)
    if a==b:
        print('success')
        print(a,b)
    elif a!=b:
        print('fail')
        print(a,b)  


a=int(input('please enter a number between 1 and 100'))

comparison(a)



