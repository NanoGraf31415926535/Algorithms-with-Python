**Explanation:**

1.  **`objective_function(particle)`:** The function we want to minimize. The input `particle` is a list representing the position in the search space.
2.  **`initialize_particle(bounds)`:** Creates a dictionary representing a particle. Each particle has a `position` (current location), a `velocity` (direction and speed of movement), a `best_position` (the best position it has found so far), and `best_fitness` (the fitness at its best position). The initial position and velocity are randomized within the given bounds.
3.  **`initialize_swarm(swarm_size, bounds)`:** Creates a list of `swarm_size` particles.
4.  **`update_velocity(particle, global_best_position, ...)`:** Updates the velocity of a particle based on three components:
    * **Inertia:** The particle's previous velocity, weighted by `inertia_weight`. This helps the particle continue moving in its current direction.
    * **Cognitive (Personal Best):** The attraction of the particle towards its own best-found position, weighted by `cognitive_coefficient` and a random factor.
    * **Social (Global Best):** The attraction of the particle towards the best position found by the entire swarm, weighted by `social_coefficient` and a random factor.
5.  **`update_position(particle, bounds)`:** Updates the particle's position by adding its current velocity. Simple clamping is used to ensure the particle stays within the defined `bounds`.
6.  **`particle_swarm_optimization(...)`:**
    * **Initialization:** Creates the initial swarm and finds the `global_best_particle` based on the initial best fitnesses.
    * **Iteration:** The algorithm iterates for a specified number of `iterations`.
        * For each `particle` in the `swarm`:
            * Its `velocity` is updated.
            * Its `position` is updated.
            * The `current_fitness` at the new position is evaluated.
            * The particle's `best_position` and `best_fitness` are updated if the current position is better.
            * The `global_best_particle` is updated if the current particle's best fitness is better than the global best.
        * The progress (iteration, global best fitness, global best position) is recorded in `history`.
    * **Return:** The algorithm returns the `best_position` found by the swarm, its `best_fitness`, and the `history` of the optimization process.