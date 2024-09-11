def calculate_total(items):
    total = 0
    # On parcourt tous les items de la commande
    for item in items:
        # Si c'est de la nourriture, on applique une taxe de 10%
        if item["category"] == "food":
            total += item["price"] * 1.1
        # Sinon, on applique une taxe standard de 5%
        else:
            total += item["price"] * 1.05
    return total
