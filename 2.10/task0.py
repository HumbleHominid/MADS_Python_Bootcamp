import numpy as np

stock_prices = np.array(
    [150.2, 152.5, 148.9, 155.3, 157.8, 153.6, 150.0, 149.5, 151.2, 154.1]
)
mean = np.mean(stock_prices)
std = np.std(stock_prices)
print(f"Average stock price: {mean:.2f}")
print(f"Highest stock price: {np.max(stock_prices):.2f}")
print(f"Lowest stock price: {np.min(stock_prices):.2f}")
print(f"Standard deviation of stock prices: {std:.2f}")

normalized_stock_prices = stock_prices.copy()
normalized_stock_prices -= mean
normalized_stock_prices /= std
normalized_stock_prices_as_strings = [f"{i:.8f}" for i in normalized_stock_prices]

print(f"Normalized stock prices: {', '.join(normalized_stock_prices_as_strings)}")
