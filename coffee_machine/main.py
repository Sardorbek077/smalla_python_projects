from types_of_coffee import coffee_names

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18},
        'cost': 10,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 25},
        'cost': 14,
    },
    'capuccino': {
        'ingredients': {
            'water': 50,
            'coffee': 18},
        'cost': 10,
    }
}

sufficient_materials = {
    'water': 1000,
    'milk': 500,
    'coffee': 200,
    'money': 0
}


def is_sufficient(order_ingredients):
    """Return True when there is enough resources, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= sufficient_materials[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


def process_payment():
    """Return the total calculations from coins inserted."""
    print('Please insert coins.')
    total = int(input('How many 50 grosz?: ')) * 50
    total += int(input('How many 1 zloty?: ')) * 100
    total += int(input('How many 2 zloty?: ')) * 200
    total += int(input('How many 5 zloty?: ')) * 500
    return total/100


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient."""
    global profit
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is {change} zloty in change.")
        profit += drink_cost
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


def make_coffee(coffee_name, order_ingredients):

    for item in order_ingredients:
        sufficient_materials[item] -= order_ingredients[item]
        sufficient_materials['money'] += profit
    print(f'Here\'s your {coffee_name} 😊')


profit = 0

is_off = False


while not is_off:
    for keys, values in coffee_names.items():
        print(f'{keys}: {values} {MENU[values]["cost"]}zl')
    choice = input('What would you like? Please write in numbers: ')
    if choice == 'off':
        is_off = True
    elif choice == 'report':
        print(f"water: {sufficient_materials['water']}ml")
        print(f"milk: {sufficient_materials['milk']}ml")
        print(f"coffee: {sufficient_materials['coffee']}g")
        print(f"money: {profit}zl")
    else:
        drink = MENU[coffee_names[int(choice)]]
        if is_sufficient(drink['ingredients']):
            payment = process_payment()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(coffee_names[int(choice)], drink['ingredients'])

