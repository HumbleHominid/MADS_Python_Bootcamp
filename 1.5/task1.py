def get_int_input() -> int:
    while True:
        user_input = input("> ")
        try:
            res = int(user_input)
            return res
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_float_input() -> float:
    while True:
        user_input = input("> ")
        try:
            res = float(user_input)
            return res
        except ValueError:
            print("Invalid input. Please enter a valid float.")


print("Enter the initial stock price:")
initial_price = get_float_input()
print("Enter the monthy return (in %):")
monthly_return = get_float_input()
print("Enter the number of months:")
months = get_int_input()

final_price = initial_price * (1 + monthly_return / 100) ** months
print(f"Final stock price after {months} months: {final_price:.2f}")
