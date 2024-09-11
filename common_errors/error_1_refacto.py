def calculate_item_price(item: dict) -> float:
    tax_rates = {
        "food": 1.1,
        "clothing": 1.05,
        "electronics": 1.2
    }
    return item["price"] * tax_rates.get(item["category"], 1)


def calculate_delivery_cost(order) -> int:
    return 15 if order["delivery"] == "express" else 5


def process_order(order: dict) -> float:
    total = sum(calculate_item_price(item) for item in order["items"])
    total += calculate_delivery_cost(order)
    return total
