from abc import ABC, abstractmethod

# Interfaces spécifiques
class SwimmerInterface(ABC):
    @abstractmethod
    def swim(self) -> None:
        pass

class WeightLifterInterface(ABC):
    @abstractmethod
    def lift_weights(self) -> None:
        pass

class YogiInterface(ABC):
    @abstractmethod
    def do_yoga(self) -> None:
        pass

# Classe pour les nageurs
class Swimmer(SwimmerInterface):
    def swim(self) -> None:
        print("Swimming in the pool")

# Classe pour les haltérophiles
class WeightLifter(WeightLifterInterface):
    def lift_weights(self) -> None:
        print("Lifting weights in the gym")

# Classe pour les yogis
class Yogi(YogiInterface):
    def do_yoga(self) -> None:
        print("Doing yoga in the studio")

# Utilisation
swimmer = Swimmer()
swimmer.swim()

weight_lifter = WeightLifter()
weight_lifter.lift_weights()

yogi = Yogi()
yogi.do_yoga()