from sre_constants import CATEGORY
from unicodedata import category


starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}

total_spend=0

print('The most expensive items in each category are:')

for menu in [starters, mains, desserts, beers]:
    price=max(menu.values()) # pick up highest price in each category
    for order in menu.items(): # check each item
        if price in order: # find the item
            print(order[0],'-',order[1])
            total_spend=total_spend + price

print('Dot need to pay', total_spend,'for all, plus', total_spend/10, 'tax')
