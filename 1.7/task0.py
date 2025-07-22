import sys


def convert_float(val: str) -> float:
    try:
        usd = float(val)
        return usd
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        sys.exit(1)


def assert_positive(val: float) -> None:
    if val <= 0:
        print("Error: Please enter a positive number.")
        sys.exit(1)


usd_input = input("Amount of USD to convert to EUR: ")
usd = convert_float(usd_input)
assert_positive(usd)
exchange_rate_input = input("Current exchange rate (USD to EUR): ")
exchange_rate = convert_float(exchange_rate_input)
assert_positive(exchange_rate)

print(f"{usd:,.2f} USD -> {usd * exchange_rate:,.2f} EUR")
