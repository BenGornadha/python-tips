from typing import List


def calculate_commission(sales: List[dict], target_product: str) -> float:
    total_commission = 0
    for sale in sales:
        product = sale['product']
        amount = sale['amount']
        if product == target_product:
            commission_rate = 0.2
        else:
            commission_rate = 0.1
        total_commission += amount * commission_rate
    return total_commission
























def calculate_total_commission(sales: List[dict], target_product: str) -> float:
    total_commission = 0
    for sale in sales:
        commission = calculate_commission_for_sale(sale, target_product)
        total_commission += commission
    return total_commission


def calculate_commission_for_sale(sale: dict, target_product: str) -> float:
    commission_rate = get_commission_rate(sale['product'], target_product)
    return sale['amount'] * commission_rate


def get_commission_rate(product: str, target_product: str) -> float:
    if product == target_product:
        return 0.2
    return 0.1
