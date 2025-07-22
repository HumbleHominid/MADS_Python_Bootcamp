import sys


class ValueException(ValueError):
    pass


def break_even(
    initial_investment: float,
    monthly_cashflow: float,
    discount_rate: float,
    months: int = 0,
) -> int:
    # Safety limit to prevent infinite recursion
    if months >= sys.getrecursionlimit() * 0.95:
        raise ValueException(
            "Break-even point not reached within a reasonable timeframe."
        )
    monthly_discount_rate = discount_rate / 100 / 12
    new_balance = initial_investment * (1 + monthly_discount_rate) + monthly_cashflow
    if new_balance >= 0:
        return months + 1

    return break_even(new_balance, monthly_cashflow, discount_rate, months + 1)


if __name__ == "__main__":
    initial_investment = -20000
    monthly_cashflow = 84
    discount_rate = 5

    months_to_recovery = break_even(initial_investment, monthly_cashflow, discount_rate)
    print(f"Months until full recovery: {months_to_recovery}")
