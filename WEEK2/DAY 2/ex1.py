

"""Create another cat breed named Siamese which inherits from the Cat class.
Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
Take all the cats for a walk, use the walk method."""

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Creating instances of each cat breed
bengal_cat = Bengal('Bengie', 2)
chartreux_cat = Chartreux('Charty', 3)
siamese_cat = Siamese('Simmy', 1)

# Creating a list of all cats
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Creating an instance of the Pets class with all the cats
sara_pets = Pets(all_cats)

# Taking all the cats for a walk
sara_pets.walk()
