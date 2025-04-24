**Explanation:**

1.  **`objective_function(individual)`:** This is the function we want to *maximize* in a typical GA context (fitness). Since our previous examples were about minimization, we're maximizing the negative of that function here.
2.  **`generate_individual(bounds)`:** Creates a random individual (a list of parameters) within the specified bounds for each parameter.
3.  **`generate_population(population_size, bounds)`:** Creates an initial population of random individuals.
4.  **`evaluate_fitness(population)`:** Calculates the fitness of each individual in the population using the `objective_function`.
5.  **`selection(ranked_population, selection_rate=0.5)`:** Selects the individuals with the highest fitness to become parents for the next generation. We sort the population by fitness and retain a fraction (`selection_rate`) of the top individuals.
6.  **`crossover(parent1, parent2, crossover_rate=0.8)`:** With a certain probability (`crossover_rate`), this function combines the genetic material of two parents to create two offspring. A single-point crossover is used here, where a random point is chosen, and the genes are swapped.
7.  **`mutate(individual, mutation_rate=0.1, step_size=0.1)`:** Introduces random changes (mutations) to the genes of an individual with a certain probability (`mutation_rate`). The mutation adds a small random value within a `step_size`.
8.  **`genetic_algorithm(...)`:**
    * **Initialization:** Creates an initial population.
    * **Generational Loop:** Iterates for a specified number of `generations`.
        * **Evaluation:** Evaluates the fitness of the current population.
        * **Selection:** Selects the parents for the next generation.
        * **Crossover:** Creates offspring by combining parents.
        * **Mutation:** Applies random mutations to the offspring.
        * **Population Replacement:** The new generation consists of the selected parents and the offspring.
        * **History Tracking:** Records the best fitness and individual in each generation.
    * **Final Result:** Returns the best individual found and its fitness.

This implementation provides a basic understanding of how a Genetic Algorithm works using standard Python libraries. More advanced GA implementations often involve different selection methods, crossover operators, mutation strategies, and handling of constraints.