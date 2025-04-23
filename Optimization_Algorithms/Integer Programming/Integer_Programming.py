from pulp import *

# Example Integer Programming Problem:
# Maximize Z = 3x + 4y
# Subject to:
# x + 2y <= 10
# 2x + y <= 8
# x >= 0, integer
# y >= 0, integer

# Create the LP problem (we'll use LpMaximize for maximization)
prob = LpProblem("Integer_Programming_Example", LpMaximize)

# Define the decision variables
# LpVariable("Variable Name", lower bound, upper bound, variable type)
x = LpVariable("x", lowBound=0, cat='Integer')
y = LpVariable("y", lowBound=0, cat='Integer')

# Define the objective function
prob += 3 * x + 4 * y, "Total_Profit"

# Define the constraints
prob += x + 2 * y <= 10, "Assembly_Constraint"
prob += 2 * x + y <= 8, "Finishing_Constraint"

# Solve the IP problem
prob.solve()

# Print the status of the solution
print("Status:", LpStatus[prob.status])

# Print the optimal value of the objective function
print("Optimal Total Profit =", value(prob.objective))

# Print the optimal values of the variables
for v in prob.variables():
    print(v.name, "=", v.varValue)