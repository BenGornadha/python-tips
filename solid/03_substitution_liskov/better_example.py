from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def se_deplacer(self) -> str:
        pass

class OiseauVolant(Animal):
    def se_deplacer(self) -> str:
        return "L'oiseau vole dans le ciel"

class OiseauNonVolant(Animal):
    def se_deplacer(self) -> str:
        return "L'oiseau marche ou nage"

class Aigle(OiseauVolant):
    pass

class Pingouin(OiseauNonVolant):
    pass

# Utilisation
def faire_voler(animal: OiseauVolant) -> None:
    print(animal.se_deplacer())

aigle = Aigle()
pingouin = Pingouin()

faire_voler(aigle)     # "L'oiseau vole dans le ciel"
faire_voler(pingouin)  # "L'oiseau marche ou nage"