"""
class Farm:
    def __init__(self,farm_name):
        self.name=farm_name
        self.animals = []
    def add_animal(self,new_animal:str, amount=1):
        if amount==1:
            self.animals.append(new_animal)
        elif amount>1:
            i=0
            while i<amount:
                self.animals.append(new_animal)   
                i+=1    
    def get_info(self,animals:list):
        # Function to generate the McDonald's farm output
        print("McDonald's farm\n")
        for animal, count in animals:
        print(f"{animal} : {count}")
    print("\n    E-I-E-I-O!")

# Example usage
animals_list = [("cow", 5), ("sheep", 2), ("goat", 12)]  # Replace with any list of animals and counts
mcdonalds_farm(animals_list)"""

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, count=1):
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        max_length = max(len(animal) for animal in self.animals.keys())
        for animal, count in self.animals.items():
            info += f"{animal.ljust(max_length)} : {count}\n"
        info += "\n    E-I-E-I-O!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        pluralized_animals = [animal + 's' if self.animals[animal] > 1 else animal for animal in animal_types]
        if len(pluralized_animals) > 1:
            animals_str = ', '.join(pluralized_animals[:-1]) + ' and ' + pluralized_animals[-1]
        else:
            animals_str = pluralized_animals[0]
        return f"{self.name}'s farm has {animals_str}."

# Example usage
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

                

"""moscow_farm=Farm('moscow')
moscow_farm.add_animal('sheep')
moscow_farm.add_animal('cow',7)
moscow_farm.information()"""

""" macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())    """