import random

def objective_function(individual):
    """The function to minimize. For GA, we often talk about fitness (to maximize),
    so we'll minimize the negative of our previous function."""
    x, y = individual
    return -(x**2 + y**2 - 4*x - 2*y + 5) # Negative for maximization

def generate_individual(bounds):
    """Generates a random individual within the given bounds."""
    return [random.uniform(b[0], b[1]) for b in bounds]

def generate_population(population_size, bounds):
    """Generates a list of random individuals."""
    return [generate_individual(bounds) for _ in range(population_size)]

def evaluate_fitness(population):
    """Evaluates the fitness of each individual in the population."""
    return [(individual, objective_function(individual)) for individual in population]

def selection(ranked_population, selection_rate=0.5):
    """Selects the top individuals for reproduction."""
    sorted_population = sorted(ranked_population, key=lambda x: x[1], reverse=True)
    retain_length = int(len(sorted_population) * selection_rate)
    return [individual for individual, fitness in sorted_population[:retain_length]]

def crossover(parent1, parent2, crossover_rate=0.8):
    """Performs crossover between two parents to create offspring."""
    if random.random() < crossover_rate:
        point = random.randint(0, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    else:
        return parent1[:], parent2[:]

def mutate(individual, mutation_rate=0.1, step_size=0.1):
    """Applies random mutations to an individual."""
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] += random.uniform(-step_size, step_size)
    return mutated_individual

def genetic_algorithm(bounds, population_size=50, generations=100, selection_rate=0.5, crossover_rate=0.8, mutation_rate=0.1, mutation_step_size=0.1):
    """A basic Genetic Algorithm."""
    population = generate_population(population_size, bounds)
    history = []

    for generation in range(generations):
        ranked_population = evaluate_fitness(population)
        best_individual, best_fitness = max(ranked_population, key=lambda x: x[1])
        history.append((generation, best_fitness, best_individual))

        parents = selection(ranked_population, selection_rate)
        offspring = []
        while len(offspring) < population_size - len(parents):
            parent1 = random.choice(parents)
            parent2 = random.choice(parents)
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            offspring.append(mutate(child1, mutation_rate, mutation_step_size))
            if len(offspring) < population_size - len(parents):
                offspring.append(mutate(child2, mutation_rate, mutation_step_size))

        population = parents + offspring

    # After all generations, find the best individual
    final_ranked_population = evaluate_fitness(population)
    best_individual, best_fitness = max(final_ranked_population, key=lambda x: x[1])

    return best_individual, best_fitness, history

# Problem definition
bounds = [(-5, 5), (-5, 5)]
population_size = 50
generations = 100

# Run the genetic algorithm
best_solution, best_fitness, history = genetic_algorithm(bounds, population_size, generations)

print("Optimal solution found:", best_solution)
print("Fitness (maximized negative of original function):", best_fitness)
print("Original function value (minimized):", -best_fitness)

# Optional: Print the history of the best fitness
# for gen, fitness, _ in history:
#     print(f"Generation {gen}: Best Fitness = {fitness}")