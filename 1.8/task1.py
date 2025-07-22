def calculate_monthly_payment(principal: float, annual_rate: float, years: int):
    monthly_interest_rate = annual_rate / 100 / 12
    total_payments = years * 12
    numerator = monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
    denominator = (1 + monthly_interest_rate) ** total_payments - 1
    return principal * numerator / denominator


if __name__ == "__main__":
    monthly_payment = calculate_monthly_payment(100000, 5, 15)
    print(f"Monthly payment: ${monthly_payment:.2f}")
