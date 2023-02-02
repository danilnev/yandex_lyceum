def choose_coffee(*args):
    global ingredients, coffies
    for coffee in args:
        if coffies[coffee][0] <= ingredients[0] and coffies[coffee][1] <= ingredients[1] and \
                coffies[coffee][2] <= ingredients[2]:
            for i in range(len(ingredients)):
                ingredients[i] -= coffies[coffee][i]
            return coffee
    return 'К сожалению, не можем предложить Вам напиток'


coffies = {
    'Эспрессо': [1, 0, 0],
    'Капучино': [1, 3, 0],
    'Маккиато': [2, 1, 0],
    'Кофе по-венски': [1, 0, 2],
    'Латте Маккиато': [1, 2, 1],
    'Кон Панна': [1, 0, 1]
}

# ingredients = [4, 4, 0]
# print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
# print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
# print(choose_coffee("Капучино", "Маккиато", "Эспрессо"))
