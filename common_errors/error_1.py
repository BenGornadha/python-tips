
def process_order(order):
    total = 0
    for item in order["items"]:
        if item["category"] == "food":
            total += item["price"] * 1.1
        elif item["category"] == "clothing":
            total += item["price"] * 1.05
        elif item["category"] == "electronics":
            total += item["price"] * 1.2
    if order["delivery"] == "express":
        total += 15
    else:
        total += 5
    return total