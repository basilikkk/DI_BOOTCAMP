class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members is not None else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(member)

# Create an instance of the Family class
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

smith_family = Family("Smith", members)

# Call all the methods
smith_family.family_presentation()

# Add a new member
smith_family.born(name='Emma', age=0, gender='Female', is_child=True)

# Check if a family member is over 18
print(smith_family.is_18('Michael'))  # True
print(smith_family.is_18('Emma'))     # False

# Presentation after new member is born
smith_family.family_presentation()


#ex5

class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power is {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old.")
                return
        print(f"{name} not found in the family.")

    def incredible_presentation(self):
        print("Here is our powerful family:")
        super().family_presentation()

# Create an instance of the Incredibles class with initial members
incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_family = TheIncredibles("Incredibles", incredibles_members)

# Call the incredible_presentation method
incredibles_family.incredible_presentation()

# Add a new member using the born method
incredibles_family.born(name='Baby Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='JackJack')

# Call the incredible_presentation method again
incredibles_family.incredible_presentation()

# Try using a power
try:
    incredibles_family.use_power('Michael')  # Should print Michael's power
    incredibles_family.use_power('Baby Jack')  # Should raise an exception
except Exception as e:
    print(e)