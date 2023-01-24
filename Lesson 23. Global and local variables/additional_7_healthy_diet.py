def diet(products: str):
    global food
    not_diet_count = 0
    for product in products.split(', '):
        if product not in food['диетическое']:
            not_diet_count += 1
    if not_diet_count > len(products.split(', ')) // 2:
        return 'Не ешь столько, По!'
    else:
        return 'Так держать, Воин Дракона!'
