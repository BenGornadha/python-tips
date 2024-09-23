from abc import ABC, abstractmethod

# Interface unique pour toutes les activités sportives
class SportClubMember(ABC):
    @abstractmethod
    def swim(self) -> None:
        pass

    @abstractmethod
    def lift_weights(self) -> None:
        pass

    @abstractmethod
    def do_yoga(self) -> None:
        pass

# Classe qui veut juste utiliser la piscine
class Swimmer(SportClubMember):
    def swim(self) -> None:
        print("Swimming in the pool")

    def lift_weights(self) -> None:
        raise NotImplementedError("I don't need this")

    def do_yoga(self) -> None:
        raise NotImplementedError("I don't need this")

# Classe qui veut juste soulever des poids
class WeightLifter(SportClubMember):
    def swim(self) -> None:
        raise NotImplementedError("I don't need this")

    def lift_weights(self) -> None:
        print("Lifting weights in the gym")

    def do_yoga(self) -> None:
        raise NotImplementedError("I don't need this")