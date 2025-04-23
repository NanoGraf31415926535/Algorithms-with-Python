**Explanation:**

1.  **`objective_function(x)`:** This remains the same, the function we want to minimize.
2.  **`generate_neighbor(solution, step_size=0.1)`:** This function creates a neighboring solution by taking the current solution and adding a small random value (within `-step_size` to `step_size`) to each of its components. The `step_size` controls how far the algorithm explores in each step.
3.  **`simulated_annealing(...)`:**
    * **Initialization:**
        * `current_solution`: Starts with the `initial_solution`.
        * `best_solution`: Keeps track of the best solution found so far.
        * `current_energy`, `best_energy`: The objective function values for the current and best solutions.
        * `temperature`: The initial temperature, which controls the probability of accepting worse solutions.
        * `cooling_rate`: A factor (between 0 and 1) by which the temperature is reduced in each iteration.
        * `num_iterations`: The total number of steps the algorithm will take.
        * `history`: A list to store the progress of the algorithm (optional, for analysis).
    * **Iteration:** The algorithm iterates for a specified number of times.
        * A `neighbor_solution` is generated.
        * The neighbor is clipped to stay within the defined `bounds`.
        * The energy (objective function value) of the neighbor is calculated.
        * `delta_energy`: The difference in energy between the neighbor and the current solution.
        * **Acceptance Criterion:**
            * If the neighbor's energy is lower (`delta_energy < 0`), it's always accepted as the new `current_solution`.
            * If the neighbor's energy is higher, it's accepted with a probability calculated using the Metropolis criterion: $P(\text{accept}) = e^{-\frac{\Delta E}{T}}$, where $\Delta E$ is the energy difference and $T$ is the current temperature. Higher temperatures and smaller energy differences lead to a higher probability of acceptance.
        * If the new `current_energy` is better than the `best_energy` found so far, the `best_solution` and `best_energy` are updated.
        * **Cooling:** The `temperature` is reduced by multiplying it with the `cooling_rate`. This gradually decreases the probability of accepting worse solutions, allowing the algorithm to converge towards a minimum.
        * The current state is recorded in the `history`.
    * **Return:** The algorithm returns the `best_solution` found, its `best_energy`, and the `history` of the process.

**How to Run:**

Save this code as a Python file (e.g., `simulated_annealing_standard.py`) and run it. You should see the "optimal" solution and its value. Keep in mind that because it's a stochastic algorithm, the result might vary slightly between runs. You can experiment with the `initial_temperature`, `cooling_rate`, `num_iterations`, and `step_size` to see how they affect the performance.

This implementation provides a basic understanding of how Simulated Annealing works using only standard Python libraries. The `scipy.optimize.dual_annealing` function is a more sophisticated version that often performs better in practice.