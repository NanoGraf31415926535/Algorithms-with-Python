# Optimization Algorithms and how they work(with examples)

**1. Linear Programming (LP)**

* **Concept:** Linear Programming is used to find the best outcome (maximum profit or minimum cost) in a mathematical model whose requirements are represented by linear relationships. You have an objective function (what you want to optimize) and a set of linear constraints (limitations or requirements).
* **Example:** A small furniture company makes tables and chairs.
    * Each table requires 2 hours of assembly and 1 hour of finishing.
    * Each chair requires 1 hour of assembly and 2 hours of finishing.
    * There are 80 hours of assembly time available per week and 70 hours of finishing time.
    * Each table yields a profit of €30, and each chair yields a profit of €20.
    * **Objective:** Maximize the total profit.
    * **Constraints:**
        * Assembly time: $2 \times (\text{number of tables}) + 1 \times (\text{number of chairs}) \leq 80$
        * Finishing time: $1 \times (\text{number of tables}) + 2 \times (\text{number of chairs}) \leq 70$
        * Number of tables $\geq 0$
        * Number of chairs $\geq 0$
* **Solution Idea:** The solution involves finding the number of tables and chairs to produce that satisfies all the constraints and yields the highest profit. Graphically, this can be seen as finding the corner point of the feasible region (defined by the inequalities) that lies on the highest profit line. Algorithms like the Simplex method systematically explore these corner points to find the optimum.

**2. Integer Programming (IP)**

* **Concept:** Integer Programming is similar to Linear Programming, but it adds the requirement that one or more of the decision variables must be integers. This is useful for problems where you can't have fractional amounts (e.g., you can't produce half a chair).
* **Example:** Consider the same furniture company, but now, for logistical reasons, they can only produce a whole number of tables and chairs. The objective and constraints remain the same.
* **Solution Idea:** Because of the integer constraint, the optimal solution might not occur at the same continuous point as in the LP problem. Algorithms for IP, like Branch and Bound, work by solving the LP relaxation (ignoring integer constraints) and then systematically branching on variables that are not integers, adding new constraints to force them to integer values. This creates a tree of subproblems that are solved until an integer optimal solution is found.

**3. Simulated Annealing (SA)**

* **Concept:** Simulated Annealing is a probabilistic optimization technique inspired by the physical process of annealing in materials science. It's used for finding good solutions to complex optimization problems, especially those with many local optima.
* **Example:** Imagine you're trying to find the lowest point in a very bumpy landscape (the objective function), but you can only see a small area around you. You might get stuck in a local valley (local optimum). SA helps you escape by allowing occasional "uphill" moves (accepting worse solutions) with a probability that decreases as the "temperature" (a control parameter) cools down.
* **Solution Idea:** SA starts with a random solution. In each step, it generates a neighbor of the current solution. If the neighbor is better, it's always accepted. If it's worse, it's accepted with a probability that depends on how much worse it is and the current temperature. As the algorithm progresses, the temperature decreases, making it less likely to accept worse solutions, thus converging towards a global optimum.

**4. Genetic Algorithms (GA)**

* **Concept:** Genetic Algorithms are inspired by natural selection and genetics. They work with a population of potential solutions (individuals) and iteratively improve them through processes like selection, crossover (combining solutions), and mutation (random changes).
* **Example:** Suppose you need to design the most aerodynamic shape for a car (the objective function). You start with a population of different car shapes. The "fitness" of each shape is evaluated (how aerodynamic it is). The best shapes are more likely to "reproduce" (crossover their features) to create new shapes, and random mutations are introduced to explore new possibilities. Over generations, the population evolves towards more aerodynamic designs.
* **Solution Idea:** GA maintains a population of solutions. In each generation:
    1.  **Selection:** Individuals with higher fitness are selected to become parents.
    2.  **Crossover:** Parents' "genes" (parameters of the solution) are combined to create offspring.
    3.  **Mutation:** Random changes are introduced in some offspring.
    4.  The new population replaces the old one, and the process repeats.

**5. Particle Swarm Optimization (PSO)**

* **Concept:** Particle Swarm Optimization is a computational method inspired by the social behavior of bird flocking or fish schooling. A "swarm" of particles moves through the search space, and each particle's movement is influenced by its own best-found position and the best-found position of the entire swarm.
* **Example:** Imagine a flock of birds searching for the location with the most food (the optimum). Each bird individually explores, remembers the best spot it has found so far, and is also attracted to the best spot found by the entire flock. This collective intelligence helps the swarm converge towards the food source.
* **Solution Idea:** PSO starts with a population of particles with random positions and velocities in the search space. In each iteration:
    1.  Each particle updates its velocity based on:
        * Its previous velocity.
        * The difference between its current position and its personal best position found so far.
        * The difference between its current position and the global best position found by the entire swarm.
    2.  Each particle updates its position based on its new velocity.
    The particles "fly" through the search space, guided by their own experience and the collective experience of the swarm, towards the optimal solution.