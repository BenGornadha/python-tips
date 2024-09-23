class EspressoCapsule:
    def brew(self) -> None:
        print("Brewing an espresso")

class CappuccinoCapsule:
    def brew(self) -> None:
        print("Brewing a cappuccino")

class CoffeeMachine:
    def brew_espresso(self) -> None:
        capsule = EspressoCapsule()
        capsule.brew()

    def brew_cappuccino(self) -> None:
        capsule = CappuccinoCapsule()
        capsule.brew()

# Utilisation
machine = CoffeeMachine()
machine.brew_espresso()  # Dépend de EspressoCapsule
machine.brew_cappuccino()  # Dépend de CappuccinoCapsule