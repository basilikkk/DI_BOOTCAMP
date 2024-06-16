import string
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self,new_animal):
        self.animals.append(new_animal)
    def get_animal(self):
        for i in range(len(self.animals)):
            print(self.animals[i])
    def sell_animal(self,sold_animal):
        if sold_animal in self.animals:
            self.animals.remove(sold_animal)       
    def sort_animal(self):
        alphabet_dict = {letter: [] for letter in string.ascii_lowercase} 
        for item in self.animals:
            first_letter = item[0].lower()
            if first_letter in alphabet_dict:
                alphabet_dict[first_letter].append(item)
        print(alphabet_dict)


ramat_gan_safari=Zoo('MOSCOW_ZOO')

ramat_gan_safari.add_animal('girafe')
ramat_gan_safari.add_animal('monkey')
ramat_gan_safari.sell_animal('monkey')
ramat_gan_safari.add_animal('girafe')
ramat_gan_safari.add_animal('horse')
ramat_gan_safari.add_animal('hippo')
ramat_gan_safari.get_animal()
ramat_gan_safari.sort_animal()



    



