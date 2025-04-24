from pyswarm import pso
import numpy as np

# Example function to minimize
def objective_function_pso(x):
    return x[0]**2 + x[1]**2 - 4*x[0] - 2*x[1] + 5

# Bounds for the variables
lb = [-5, -5]  # Lower bounds for x and y
ub = [5, 5]    # Upper bounds for x and y

# Perform particle swarm optimization
xopt, fopt = pso(objective_function_pso, lb, ub, swarmsize=50, maxiter=100)

print("Optimal solution (xopt):", xopt)
print("Optimal value (fopt):", fopt)