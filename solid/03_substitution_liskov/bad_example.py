class Animal:
    def se_deplacer(self) -> str:
        return "L'animal se déplace"

class Oiseau(Animal):
    def se_deplacer(self) -> str:
        return "L'oiseau vole dans le ciel"

class Pingouin(Oiseau):
    def se_deplacer(self) -> str:
        return "Le pingouin nage dans l'eau"

# Utilisation
def faire_voler(oiseau: Oiseau) -> None:
    print(oiseau.se_deplacer())

aigle = Oiseau()
pingouin = Pingouin()

faire_voler(aigle)     # Fonctionne : "L'oiseau vole dans le ciel"
faire_voler(pingouin)   # Problème : "Le pingouin nage dans l'eau" (on s'attend à ce qu'il vole)