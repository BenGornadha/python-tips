from abc import ABC, abstractmethod

class CapsuleInterface(ABC):
    @abstractmethod
    def brew(self) -> None:
        pass

class EspressoCapsule(CapsuleInterface):
    def brew(self) -> None:
        print("Brewing an espresso")

class CappuccinoCapsule(CapsuleInterface):
    def brew(self) -> None:
        print("Brewing a cappuccino")

class CoffeeMachine:
    def __init__(self, capsule: CapsuleInterface) -> None:
        self.capsule = capsule

    def brew(self) -> None:
        self.capsule.brew()

# Utilisation
espresso_capsule = EspressoCapsule()
cappuccino_capsule = CappuccinoCapsule()

machine = CoffeeMachine(espresso_capsule)
machine.brew()  # "Brewing an espresso"

machine = CoffeeMachine(cappuccino_capsule)
machine.brew()  # "Brewing a cappuccino"