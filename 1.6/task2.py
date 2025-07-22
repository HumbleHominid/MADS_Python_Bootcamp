inventory = {
    "Electronics": {"Laptops": 15, "Headphones": 30, "Monitors": 12},
    "Furniture": {"Sofas": 5, "Chairs": 10, "Tables": 7},
}

print(f"There are {inventory["Electronics"]["Laptops"]} laptops in stock.")
inventory["Furniture"]["Sofas"] += 5
del inventory["Furniture"]["Chairs"]
print(f"Inventory categories: {', '.join(inventory.keys())}")
print(f"Electronics subcategories: {', '.join(inventory['Electronics'].keys())}")
