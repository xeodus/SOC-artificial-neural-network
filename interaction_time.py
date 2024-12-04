import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Simulation parameters
num_particles = 100
num_receptors = 70
box_size = 10.0
time_step = 0.1
collision_threshold = 0.1
num_iterations = 500

def initialize_particles(num_particles, num_receptors, box_size):
    particles = [{'label': i + 1, 'position': np.random.rand() * box_size, 'velocity': 0.0} for i in range(num_particles)]
    for i in range(num_receptors):
        particles[i]['label'] = f'R{i + 1}'  # Labeling receptors
    return particles

def update_particle_positions(particles, time_step):
    for i in particles:
        particles['position'][i] += np.random.normal(0.0, 1.0) * time_step
        return particles

def check_collision(particles, collision_threshold, num_receptors):
    for i in range(num_receptors, len(particles)):
        for j in range(num_receptors):
            if abs(particles[i]['position'] - particles[j]['position']) < collision_threshold:
                return True, i, j
    return False, None, None

def update_transmitter_position(particles, transmitter_index, receptor_index, box_size):
    particles[transmitter_index]['position'] = np.random.rand() * box_size

def simulate_first_passage_time(num_particles, num_receptors, box_size, time_step, collision_threshold):
    particles = initialize_particles(num_particles, num_receptors, box_size)
    time_elapsed = 0.0
    
    while True:
        collision, transmitter_index, receptor_index = check_collision(particles, collision_threshold, num_receptors)
        if collision:
            update_transmitter_position(particles, transmitter_index, receptor_index, box_size)
            time_elapsed += time_step
        else:
            break
    
    return time_elapsed

# Run the simulation for multiple iterations
first_passage_times = []

for _ in range(num_iterations):
    first_passage_time = simulate_first_passage_time(num_particles, num_receptors, box_size, time_step, collision_threshold)
    first_passage_times.append(first_passage_time)

# Calculate and print the average first passage time
average_first_passage_time = np.mean(first_passage_times)
print(f"Average First Passage Time over {num_iterations} iterations: {average_first_passage_time}")

# Plot
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(range(1, num_iterations + 1), first_passage_times, marker='o', markeredgecolor='red', markerfacecolor='red', linestyle='-', color='blue')
ax.set_xlabel('Iterations', fontsize=12)
ax.set_ylabel('First Passage Time', fontsize=12)
ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))
ax.yaxis.set_major_locator(MaxNLocator(nbins=10))
ax.tick_params(axis='both', which='major',labelsize=12, width=1.5)
ax.text(num_iterations // 2, min(first_passage_times) + 0.5, f'70 receptors system: {average_first_passage_time:.2f}', color='black', fontsize=12)
ax.grid(True, linestyle='--', linewidth=0.5)
plt.show()