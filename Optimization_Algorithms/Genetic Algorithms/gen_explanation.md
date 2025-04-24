**Explanation of the `DEAP` Implementation:**

1.  **Import Libraries:** We import `numpy` for numerical operations and the necessary modules from `deap`.
2.  **Define Problem Parameters:** We set the size of an individual, the population size, crossover and mutation probabilities, the number of generations, a random seed for reproducibility, and the bounds for the variables.
3.  **Create Types (`creator`):**
    * `creator.create("FitnessMin", base.Fitness, weights=(-1.0,))`: We create a fitness class named `FitnessMin` that inherits from `base.Fitness`. The `weights=(-1.0,)` indicates that we want to minimize the objective function (a weight of -1 means lower values are better).
    * `creator.create("Individual", list, fitness=creator.FitnessMin)`: We create an `Individual` class that is a list (representing the parameters $x$ and $y$) and has the `FitnessMin` fitness attribute.
4.  **Initialize Toolbox (`toolbox`):** The `toolbox` is a container for functions used in the GA.
    * `toolbox.register("attr_float", np.random.uniform, BOUNDS[0][0], BOUNDS[0][1])`: We register a function to generate random floating-point numbers within the specified bounds.
    * `toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=INDIVIDUAL_SIZE)`: We register a function to create an individual by repeating the `attr_float` function `INDIVIDUAL_SIZE` times.
    * `toolbox.register("population", tools.initRepeat, list, toolbox.individual)`: We register a function to create a population as a list of individuals.
    * `toolbox.register("evaluate", eval_func)`: We register our `eval_func` as the function to evaluate the fitness of an individual. It returns the fitness as a tuple (as required by `DEAP`).
    * `toolbox.register("select", tools.selTournament, tournsize=3)`: We register the tournament selection operator, where `tournsize` specifies the number of individuals participating in each tournament.
    * `toolbox.register("mate", tools.cxBlend, alpha=0.5)`: We register the blended crossover operator (`cxBlend`) with an alpha of 0.5.
    * `toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)`: We register the Gaussian mutation operator (`mutGaussian`) with a mean (`mu`) of 0, a standard deviation (`sigma`) of 1, and an independent probability (`indpb`) of 0.1 for each attribute to be mutated.
5.  **Run the Genetic Algorithm (`algorithms.eaSimple`):**
    * We create an initial `population`.
    * `tools.HallOfFame(1)` (`hof`): This object will store the best individual found during the evolution.
    * `tools.Statistics(...)` (`stats`): This object will calculate statistics about the population (average, standard deviation, min, max fitness).
    * `algorithms.eaSimple(...)`: This function implements a standard evolutionary algorithm. We provide the population, toolbox, probabilities for crossover (`cxpb`) and mutation (`mutpb`), the number of generations (`ngen`), the statistics object, the hall of fame, and a verbosity flag.
6.  **Output:** After the algorithm finishes, we print the best individual found in the hall of fame and its fitness value (which is the minimum value of our objective function).