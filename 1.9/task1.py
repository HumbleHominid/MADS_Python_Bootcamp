from my_module import (
    calculate_future_value,
    get_positive_float_input,
    get_positive_int_input,
)

years = get_positive_int_input("Enter the number of years")
principal = get_positive_float_input("Enter the principal amount")
annual_rate = get_positive_float_input("Enter the annual interest rate (as %)")
compounds_per_year = get_positive_int_input(
    "Enter the number of times interest is compounded per year"
)

standard, compound = calculate_future_value(
    principal, annual_rate, years, compounds_per_year
)

print(f"Future value (standard): ${standard:,.2f}")
print(f"Future value (compound): ${compound:,.2f}")
