
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Baverages": {"coffee":2.22, "soft drink":3.00}})
#we can add it also in this way :restaurant_menu["Beverages"] = {"Coffee": 2.50, "Soft Drink": 1.99}

restaurant_menu["Main Course"].update({"Steak": 17.99})
#we can add it alsoo in this way: restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)

