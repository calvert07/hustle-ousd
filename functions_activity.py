menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

def total_price(item1, item2):
    return menu[item1] + menu[item2]

def price_difference(item1, item2):
    return abs(menu[item1] - menu[item2])

def inflation(item, multiplier):
    menu[item] = menu[item] * multiplier
    return menu

def deflation(item, divisor):
    menu[item] = menu[item] / divisor
    return menu

# Example test calls
print(total_price('Pizza', 'Burger'))
print(price_difference('Pizza', 'Burger'))
print(inflation('Pizza', 1.1))
print(deflation('Pizza', 1.1))