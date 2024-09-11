def calculate_discount(price):
    return price * 0.9

def apply_discount_to_item(item):
    item["price"] = calculate_discount(item["price"])