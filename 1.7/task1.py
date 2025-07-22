def get_int_input() -> int:
    while True:
        user_input = input("> ")
        try:
            res = int(user_input)
            return res
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


print("Input the amount of items to add:")
list_size = get_int_input()
items: list[str] = []

for i in range(list_size):
    item = input(f"Enter item {i + 1}: ")
    items.append(item)

print(f"Shopping list: {', '.join(items)}")
