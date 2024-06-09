#ex1

for i in range(4):
    print('Hello world')

print()
#ex2


print((99**3)*8) 
print()

#ex3

print('false','true','false','error','false')

print()


#ex4
computer_brand=input('please write the brand nime of your computer:')
print(f'I have a {computer_brand} computer".')
print()

#ex5
"""Create a variable called name, and set it’s value to your name.
Create a variable called age, and set it’s value to your age.
Create a variable called shoe_size, and set it’s value to your shoe size.
Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
Have your code print the info message.
Run your code"""
my_name='VASILI'
age=24
shoe_size=44.5
info=F"hi my name is {my_name}, my age is {age} and i buy shoes with {shoe_size}size "


#ex6
"""Create two variables, a and b.
Each variable value should be a number.
If a is bigger then b, have your code print Hello World."""

a=10
b=7
if a>b:
    print("hello world")


    #ex7
"""Write code that asks the user for a number and determines whether this number is odd or even.    """

number=int(input('please enter a number'))
if (number % 2==0):
    print('it is a even number')
else:
    print('it is a odd number')    
    
    print()

    #ex8
""""    Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome."""
myname="vasili"

user_name=input('please enter your name:')

if (user_name == user_name):
    print('ha-ha, we have same names')
else:
    print('i like your name')    