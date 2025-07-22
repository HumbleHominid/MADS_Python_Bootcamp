def get_float_input() -> float:
    while True:
        user_input = input("> ")
        try:
            res = float(user_input)
            return res
        except ValueError:
            print("Invalid input. Please enter a valid float.")


print("Enter the loan amount:")
credit_amount = get_float_input()
print("Enter the repayment amount:")
repayment_amount = get_float_input()
print("Enter the annual interest rate (in annual %):")
rate = get_float_input()

month = 0

while credit_amount > 0.0:
    month += 1
    # Calculate the monthly interest payment
    interest = credit_amount * rate / 100.0 / 12.0
    # Check if the repayment is more than the amount left
    if credit_amount > repayment_amount:
        # Calculate the remaining amount
        credit_amount -= repayment_amount
    else:
        # Repayment is more than the amount left
        repayment_amount = credit_amount
        credit_amount = 0.0

    print(
        f"Month: {month}, "
        + f"Repayment: {repayment_amount:.2f}, "
        + f"Interest payment: {interest:.2f}, "
        + f"Remaining: {credit_amount:.2f}"
    )
