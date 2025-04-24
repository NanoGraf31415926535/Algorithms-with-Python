import numpy as np
from deap import base, creator, tools, algorithms

# Define the problem
INDIVIDUAL_SIZE = 2
POPULATION_SIZE = 50
P_CROSSOVER = 0.9
P_MUTATION = 0.1
N_GENERATIONS = 100
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
BOUNDS = [(-5, 5), (-5, 5)]

# Create types
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize the objective function
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize toolbox
toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, BOUNDS[0][0], BOUNDS[0][1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=INDIVIDUAL_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define fitness function
def eval_func(individual):
    x, y = individual
    return (x**2 + y**2 - 4*x - 2*y + 5,),  # Return as a tuple

toolbox.register("evaluate", eval_func)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)

# Run the genetic algorithm
if __name__ == "__main__":
    population = toolbox.population(n=POPULATION_SIZE)
    hof = tools.HallOfFame(1)  # Keep track of the best individual
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)

    algorithms.eaSimple(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION, ngen=N_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    best_ind = hof.items[0]
    print("Best individual:", best_ind)
    print("Fitness of the best individual (minimized value):", best_ind.fitness.values[0])