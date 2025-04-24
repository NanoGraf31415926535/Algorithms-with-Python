import random

def objective_function(particle):
    """The function to minimize."""
    x, y = particle
    return x**2 + y**2 - 4*x - 2*y + 5

def initialize_particle(bounds):
    """Initializes a particle with a random position and velocity."""
    position = [random.uniform(b[0], b[1]) for b in bounds]
    velocity = [random.uniform(-(b[1] - b[0]) * 0.1, (b[1] - b[0]) * 0.1) for b in bounds]
    return {'position': position, 'velocity': velocity, 'best_position': list(position), 'best_fitness': objective_function(position)}

def initialize_swarm(swarm_size, bounds):
    """Initializes a swarm of particles."""
    return [initialize_particle(bounds) for _ in range(swarm_size)]

def update_velocity(particle, global_best_position, inertia_weight=0.5, cognitive_coefficient=1, social_coefficient=1):
    """Updates the velocity of a particle."""
    new_velocity = []
    for i in range(len(particle['position'])):
        inertia = inertia_weight * particle['velocity'][i]
        cognitive = cognitive_coefficient * random.random() * (particle['best_position'][i] - particle['position'][i])
        social = social_coefficient * random.random() * (global_best_position[i] - particle['position'][i])
        new_velocity.append(inertia + cognitive + social)
    return new_velocity

def update_position(particle, bounds):
    """Updates the position of a particle, ensuring it stays within the bounds."""
    new_position = []
    for i in range(len(particle['position'])):
        new_position.append(particle['position'][i] + particle['velocity'][i])
        # Keep particles within bounds (simple clamping)
        new_position[i] = max(bounds[i][0], min(bounds[i][1], new_position[i]))
    return new_position

def particle_swarm_optimization(objective_function, bounds, swarm_size=50, iterations=100, inertia_weight=0.5, cognitive_coefficient=1, social_coefficient=1):
    """A basic Particle Swarm Optimization algorithm."""
    swarm = initialize_swarm(swarm_size, bounds)
    global_best_particle = min(swarm, key=lambda p: p['best_fitness'])
    history = []

    for iteration in range(iterations):
        for particle in swarm:
            # Update velocity
            particle['velocity'] = update_velocity(particle, global_best_particle['best_position'], inertia_weight, cognitive_coefficient, social_coefficient)

            # Update position
            particle['position'] = update_position(particle, bounds)

            # Evaluate fitness of the new position
            current_fitness = objective_function(particle['position'])

            # Update personal best if the current position is better
            if current_fitness < particle['best_fitness']:
                particle['best_position'] = list(particle['position'])
                particle['best_fitness'] = current_fitness

            # Update global best if the current personal best is better
            if particle['best_fitness'] < global_best_particle['best_fitness']:
                global_best_particle = particle

        history.append((iteration, global_best_particle['best_fitness'], list(global_best_particle['position'])))

    return global_best_particle['position'], global_best_particle['best_fitness'], history

# Problem definition
bounds = [(-5, 5), (-5, 5)]
swarm_size = 50
iterations = 100

# Run the particle swarm optimization algorithm
best_position, best_fitness, history = particle_swarm_optimization(objective_function, bounds, swarm_size, iterations)

print("Optimal position found:", best_position)
print("Optimal value (min):", best_fitness)

# Optional: Print the history of the best fitness
# for iter, fitness, _ in history:
#     print(f"Iteration {iter}: Best Fitness = {fitness}")