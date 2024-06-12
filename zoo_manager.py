class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species 

    def speak(self):
        return "Animal sound"
    
class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def give_birth(self):
        return f'{self._name} the {self._species} has given birth'

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self._wingspan = wingspan


class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def bask_in_sun(self):
        return f'{self._name} the {self._species} is basking in the sun'

class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def climb_trees(self):
        return f'{self._name} the {self._species} is climbing trees'

class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def carry_baby(self):
        return f'{self._name} the {self._species} is carrying its baby'
    
class Aviary:
    def __init__(self, birds = []):
        self._birds = birds

class ReptileEnclosure:
    def __init__(self, reptiles = []):
        self._reptiles = reptiles 

mammal = Mammal("Giraffe", "Giraffa camelopardalis")
mammal.give_birth()