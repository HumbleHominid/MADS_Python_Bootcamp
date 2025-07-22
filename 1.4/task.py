principle = 1000
rate = 0.05
times_compounded = 4
years = 10

amount = principle * (1 + rate / times_compounded) ** (times_compounded * years)

print(f"Amount after {years} years: ${amount:.2f}")
