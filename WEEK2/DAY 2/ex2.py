"""Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.
"""

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f'{self.name} won the fight'
        elif my_power < other_power:
            return f'{other_dog.name} won the fight'
        else:
            return 'It is a tie'

# Create 3 instances of the Dog class
dog1 = Dog('', 4, 20)
dog2 = Dog('Rex', 5, 25)
dog3 = Dog('Milo', 3, 15)
print(dog1.bark())          
print(dog2.run_speed())     
print(dog3.run_speed())    

# Make the dogs fight each other
print(dog1.fight(dog2))     
print(dog2.fight(dog3))     
print(dog3.fight(dog1))     

