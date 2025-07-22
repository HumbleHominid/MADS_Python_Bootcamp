from my_module import calculate_stock_price

initial_price = 100.0
daily_return = 0.01
days = 28
price = calculate_stock_price(initial_price, daily_return, days)

print(f"The stock price after {days} days is: ${price:.2f}")
