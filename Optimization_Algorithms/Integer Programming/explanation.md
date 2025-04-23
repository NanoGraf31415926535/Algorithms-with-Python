**Explanation:**

1.  **Import `pulp`:** We import all the necessary components from the `pulp` library.
2.  **Create the LP Problem (`LpProblem`):** We create an instance of `LpProblem`. The first argument is a name for the problem, and the second argument (`LpMaximize`) specifies that we want to maximize the objective function.
3.  **Define Decision Variables (`LpVariable`):** We define the decision variables `x` (number of tables) and `y` (number of chairs) using `LpVariable`.
    * The first argument is the name of the variable.
    * `lowBound=0` sets the lower bound to 0.
    * `cat='Integer'` specifies that these variables must take integer values.
4.  **Define the Objective Function:** We add the objective function to the problem using the `+=` operator. The first part is the linear expression for the objective (3\*x + 4\*y), and the second part is a string name for the objective function.
5.  **Define the Constraints:** Similarly, we add the linear constraints to the problem using the `+=` operator, along with a string name for each constraint.
6.  **Solve the IP Problem (`prob.solve()`):** This line calls the solver to find the optimal solution that satisfies all the constraints and maximizes the objective function. `PuLP` uses external solvers (which might need to be installed separately for more complex problems, but often includes a default solver).
7.  **Print Results:** We then print the status of the solution (e.g., "Optimal", "Infeasible"), the optimal value of the objective function using `value(prob.objective)`, and the optimal values of the decision variables using `v.name` and `v.varValue` for each variable in `prob.variables()`.

To run this code, save it as a Python file (e.g., `integer_programming.py`) and execute it. You should see the optimal number of tables and chairs to produce (as integers) and the maximum profit the company can achieve under these constraints.