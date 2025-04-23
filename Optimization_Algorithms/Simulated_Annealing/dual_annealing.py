from scipy.optimize import dual_annealing
import numpy as np

# Example function to minimize (can be any function)
def objective_function(x):
    return x[0]**2 + x[1]**2 - 4*x[0] - 2*x[1] + 5

# Bounds for the variables
bounds = [(-5, 5), (-5, 5)]

# Perform simulated annealing
result = dual_annealing(objective_function, bounds=bounds, seed=42)

print("Optimal solution found:", result.success)
print("Optimal value (min):", result.fun)
print("Values of x and y at the optimum:", result.x)