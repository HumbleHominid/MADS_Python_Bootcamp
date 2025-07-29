import os

import numpy as np

FILEPATH = "data/company_data.csv"

raw_data = np.loadtxt(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), FILEPATH),
    delimiter=",",
    skiprows=1,
)
x, y = raw_data[:, :-1], raw_data[:, -1]
x = np.hstack((np.ones((x.shape[0], 1)), x))

theta = np.linalg.inv(x.T @ x) @ x.T @ y

print("Intercept (θ₀):", theta[0])
print("Marketing Spend Coefficient (θ₁):", theta[1])
print("R&D Investment Coefficient (θ₂):", theta[2])
print("Number of Employees Coefficient (θ₃):", theta[3])

new_company = np.array([1, 75, 88, 240])
revenue = new_company @ theta

print(f"Predicted Profit for a company: {revenue:,.2f}")
