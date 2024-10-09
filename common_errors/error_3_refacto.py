def calculate_total(items):
    total = 0
    for current_item in items:
        tax = 1.1 if current_item["category"] == "food" else 1.05
        total += current_item["price"] * tax
    return total
