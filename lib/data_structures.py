spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [n.get('name') for n in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [n for n in spicy_foods if n.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
    for n in spicy_foods:
        heat_emoji = "🌶" * n.get('heat_level')
        print(f"{n.get('name')} ({n.get('cuisine')}) | Heat Level: {heat_emoji}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for n in spicy_foods:
        if n.get('cuisine') == cuisine:
            return n

def print_spiciest_foods(spicy_foods):
    for n in spicy_foods:
        heat_emoji = "🌶" * n.get('heat_level')
        if n.get('heat_level') > 5:
            print(f"{n.get('name')} ({n.get('cuisine')}) | Heat Level: {heat_emoji}")

def get_average_heat_level(spicy_foods):
    heat_level_total = [n.get('heat_level') for n in spicy_foods]
    total = 0
    for n in heat_level_total:
        total += n
    return total / len(heat_level_total)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
