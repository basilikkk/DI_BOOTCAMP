"""class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
"""





class Cat:
    def __init__(self,  cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


first_cat=Cat('pink',22)     
second_cat=Cat('yellow',12)
third_cat=Cat('brown',13)   

old_cat=max([first_cat,second_cat,third_cat],key=lambda Cat:Cat.age)

print(old_cat.name)
print(f'The oldest cat is {old_cat.name}, and is {old_cat.age} years old.')





class Cat_1:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


first_cat_1 = Cat('pink', 22)
second_cat_1 = Cat('yellow', 12)
third_cat_1 = Cat('brown', 13)
def find_oldest_cat(cats):
    return max(cats, key=lambda cat: cat.age)
cats = [first_cat_1, second_cat_1, third_cat_1]
oldest_cat = find_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")
