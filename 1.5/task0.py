def get_int_input() -> int:
    while True:
        user_input = input("> ")
        try:
            res = int(user_input)
            return res
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


print("Enter the number of kilometers driven:")
km_driven = get_int_input()
print("Enter the number of liters of fuel used:")
liters_used = get_int_input()

fuel_consumption = liters_used / km_driven * 100
print(f"Fuel consumption: {fuel_consumption:.2f} liters per 100 km")
