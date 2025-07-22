import sys

# Exchange rate of 1 USD to given currency
# Example: (1.40, "CAD") meand 1 USD = 1.40 CAD
EXCHANGE_RATES = {
    (1.40, "CAD"),
    (0.85, "EUR"),
    (0.75, "GBP"),
}

if len(sys.argv) != 2:
    print("Usage: python task1.py <amount_in_usd>")
    sys.exit(1)

try:
    usd = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer amount in USD.")
    sys.exit(1)

print(f"Converting {usd} USD to other currencies:")

for rate, currency in EXCHANGE_RATES:
    print(f"{usd * rate:.2f} {currency}")
