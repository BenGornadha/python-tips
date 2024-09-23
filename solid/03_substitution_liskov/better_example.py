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
def faire_se_deplacer(animal: Animal) -> None:
    print(animal.se_deplacer())

aigle = Aigle()
pingouin = Pingouin()

faire_se_deplacer(aigle)     # "L'oiseau vole dans le ciel"
faire_se_deplacer(pingouin)  # "L'oiseau marche ou nage"