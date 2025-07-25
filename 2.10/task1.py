import numpy as np

np.random.seed(42)  # For reproducibility
cost_matrix = (np.random.rand(6, 4) * 40) + 10  # Scale to range [10, 50]
demand_vector = np.random.randint(50, 200, size=4)  # Random demand between 50 and 200
factory_costs = [
    sum(demand_vector * cost_matrix[i]) for i in range(cost_matrix.shape[0])
]
min_cost = min(factory_costs)
min_ind = factory_costs.index(min_cost)
print(f"Factory {min_ind} has the lowest total cost: ${min_cost:.2f} thousand")
