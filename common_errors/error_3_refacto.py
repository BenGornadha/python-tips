def calculate_total(items):
    total = 0
    for item in items:
        tax = 1.1 if item["category"] == "food" else 1.05
        total += item["price"] * tax
    return total
