import math


def calculate_stock_price(
    initial_price: float, daily_return: float, days: int
) -> float:
    return initial_price * ((1 + daily_return) ** days)


def get_positive_float_input(message: str = "") -> float:
    while True:
        try:
            user_input = float(input(f"{message}> "))
            if user_input > 0:
                return user_input
            else:
                print("Value must be positive.")
        except ValueError:
            print("Value must be a number.")


def get_positive_int_input(message: str = "") -> int:
    while True:
        try:
            user_input = int(input(f"{message}> "))
            if user_input > 0:
                return user_input
            else:
                print("Value must be positive.")
        except ValueError:
            print("Value must be an integer.")


def calculate_future_value(
    principal: float, rate: float, years: int, times_compounded: int
) -> tuple[float, float]:
    standard = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    compound = principal * math.exp(rate * years)

    return (standard, compound)
