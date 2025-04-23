**Explanation:**

1.  **Import `linprog`:** We import the necessary function from the `scipy.optimize` module.
2.  **Objective Function Coefficients (`c`):** We define the coefficients of our objective function, $Z = 3x + 4y$. Since `linprog` minimizes by default, we use the negative of the coefficients `[-3, -4]` to achieve maximization. The order corresponds to the variables $x$ and $y$.
3.  **Constraint Coefficients (`A_ub`, `b_ub`):** We define the coefficients of the inequality constraints in the form $Ax \leq b$.
    * `A = [[1, 2], [2, 1]]` represents the coefficients of $x$ and $y$ in each constraint:
        * $1x + 2y \leq ...$
        * $2x + 1y \leq ...$
    * `b = [10, 8]` represents the upper bounds of the inequalities.
4.  **Variable Bounds (`x_bounds`, `y_bounds`):** We specify the bounds for each variable. `(0, None)` means the variable is greater than or equal to 0, with no upper bound.
5.  **Solve the Problem (`linprog`):** We call the `linprog` function with the objective function coefficients, constraint coefficients and bounds, and specify the `'simplex'` method (a common algorithm for solving linear programming problems).
6.  **Output:** The `result` object contains information about the optimization process, including:
    * `result.success`: A boolean indicating if an optimal solution was found.
    * `result.fun`: The optimal value of the objective function (which is the minimum of $-Z$, so we negate it to get the maximum $Z$).
    * `result.x`: An array containing the values of the decision variables ($x$ and $y$) at the optimal solution.

To run this code, save it as a Python file (e.g., `linear_programming.py`) and execute it. You should see the optimal solution and the corresponding values of $x$ and $y$ that maximize the profit.