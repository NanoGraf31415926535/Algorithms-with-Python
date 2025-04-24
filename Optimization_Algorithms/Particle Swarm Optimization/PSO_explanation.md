**Explanation:**

1.  **Import `pso`:** We import the `pso` function from the `pyswarm` library. We also import `numpy` (though it's not directly used in this basic example, `pyswarm` often works with NumPy arrays).
2.  **Objective Function (`objective_function_pso`):** This is the function we want to minimize. It takes a list or array `x` as input, where `x[0]` represents the first variable and `x[1]` represents the second.
3.  **Bounds (`lb`, `ub`):** We define the lower bounds (`lb`) and upper bounds (`ub`) for each variable in the search space. Here, both $x$ and $y$ are bounded between -5 and 5.
4.  **Perform PSO (`pso`):**
    * We call the `pso` function, providing:
        * `objective_function_pso`: The function to be minimized.
        * `lb`: The lower bounds for the variables.
        * `ub`: The upper bounds for the variables.
        * `swarmsize`: The number of particles in the swarm (default is 30). We've set it to 50 to be consistent with our standard library implementation.
        * `maxiter`: The maximum number of iterations the algorithm will run (default is 100).
    * The `pso` function returns two values:
        * `xopt`: The optimal (or near-optimal) position found by the swarm as a NumPy array.
        * `fopt`: The optimal value of the objective function found.
5.  **Output:** We print the optimal solution (`xopt`) and the optimal function value (`fopt`).