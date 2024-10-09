tax_rates = {
    "food": 1.1,
    "clothing": 1.05,
    "electronics": 1.2
}


def calculate_item_price_with_tax(item: dict) -> float:
    tax_rate = tax_rates.get(item["category"], 1)
    return item["price"] * tax_rate


def calculate_delivery_cost(delivery_type: str) -> int:
    return 15 if delivery_type == "express" else 5


def process_order(order: dict) -> float:
    total_price_items = sum(calculate_item_price_with_tax(item=item) for item in order["items"])
    delivery_cost = calculate_delivery_cost(delivery_type=order.get("delivery", "standard"))
    return total_price_items + delivery_cost
