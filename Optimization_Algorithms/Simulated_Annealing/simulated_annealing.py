import math
import random

def objective_function(x):
    """The function to minimize."""
    return x[0]**2 + x[1]**2 - 4*x[0] - 2*x[1] + 5

def generate_neighbor(solution, step_size=0.1):
    """Generates a neighbor solution by adding a small random step."""
    neighbor = list(solution)
    for i in range(len(neighbor)):
        neighbor[i] += random.uniform(-step_size, step_size)
    return tuple(neighbor)

def simulated_annealing(initial_solution, bounds, initial_temperature=100, cooling_rate=0.95, num_iterations=1000):
    """A basic Simulated Annealing algorithm."""
    current_solution = initial_solution
    best_solution = current_solution
    current_energy = objective_function(current_solution)
    best_energy = current_energy
    temperature = initial_temperature

    history = []

    for i in range(num_iterations):
        neighbor_solution = generate_neighbor(current_solution)

        # Ensure the neighbor is within the bounds
        neighbor_solution = tuple(max(b[0], min(b[1], neighbor_solution[j])) for j, b in enumerate(bounds))

        neighbor_energy = objective_function(neighbor_solution)
        delta_energy = neighbor_energy - current_energy

        # Acceptance probability
        if delta_energy < 0:
            # Accept if the neighbor is better
            current_solution = neighbor_solution
            current_energy = neighbor_energy
            if current_energy < best_energy:
                best_solution = current_solution
                best_energy = current_energy
        else:
            # Accept with a probability based on temperature and energy difference
            probability = math.exp(-delta_energy / temperature)
            if random.random() < probability:
                current_solution = neighbor_solution
                current_energy = neighbor_energy

        # Cool down the temperature
        temperature *= cooling_rate
        history.append((temperature, current_energy, best_energy, current_solution, best_solution))

    return best_solution, best_energy, history

# Problem definition
initial_solution = (random.uniform(-5, 5), random.uniform(-5, 5))
bounds = [(-5, 5), (-5, 5)]

# Run the simulated annealing algorithm
best_solution, best_energy, history = simulated_annealing(initial_solution, bounds)

print("Optimal solution found:", best_solution)
print("Optimal value (min):", best_energy)

# You can optionally plot the history to see the annealing process
# import matplotlib.pyplot as plt
# temperatures, current_energies, best_energies, _, _ = zip(*history)
# plt.plot(temperatures)
# plt.xlabel("Iteration")
# plt.ylabel("Temperature")
# plt.title("Cooling Schedule")
# plt.show()
#
# plt.plot(current_energies, label="Current Energy")
# plt.plot(best_energies, label="Best Energy")
# plt.xlabel("Iteration")
# plt.ylabel("Energy")
# plt.title("Energy over Iterations")
# plt.legend()
# plt.show()