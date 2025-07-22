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


print("Enter the loan amount:")
loan_amount = get_float_input()
print("Enter the annual interest rate (in %):")
annual_interest_rate = get_float_input()
print("Enter the loan term in years:")
loan_term_years = get_int_input()

number_of_payments = loan_term_years * 12
monthly_interest_rate = annual_interest_rate / 100 / 12
compounded_rate = (1 + monthly_interest_rate) ** number_of_payments
numerator = monthly_interest_rate * compounded_rate
denominator = compounded_rate - 1
monthly_payment = loan_amount * numerator / denominator

print(f"Monthly payment for the loan: {monthly_payment:.2f}")
