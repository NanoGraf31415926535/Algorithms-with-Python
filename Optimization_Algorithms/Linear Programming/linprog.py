from scipy.optimize import linprog

# Example Linear Programming Problem:
# Maximize Z = 3x + 4y
# Subject to:
# x + 2y <= 10
# 2x + y <= 8
# x >= 0
# y >= 0

# Coefficients of the objective function (minimize -Z for maximization)
c = [-3, -4]

# Coefficients of the inequality constraints (Ax <= b)
A = [[1, 2], [2, 1]]
b = [10, 8]

# Bounds for the variables (x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='simplex')

print("Optimal solution found:", result.success)
print("Optimal value (max Z):", -result.fun)
print("Values of x and y at the optimum:", result.x)