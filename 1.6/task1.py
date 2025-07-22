salaries: dict[str, float] = {"Alice": 60000, "Bob": 55000, "Charlie": 70000}

print(f"Alice's salary: {salaries['Alice']:,}")
salaries["Bob"] *= 1.10
salaries["David"] = 55000

hightest_salary = max(salaries.values())
print(f"Highest salary: {hightest_salary:,}")
