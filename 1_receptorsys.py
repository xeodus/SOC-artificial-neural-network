import numpy as np
import matplotlib.pyplot as plt

def initialize_particles(num_particles, box_size):
    particles = [{'label': i + 1, 'position': np.random.rand() * box_size, 'velocity': 0.0} for i in range(num_particles)]
    particles[0]['velocity'] = 0.0  # Particle at rest
    particles[0]['label'] = 1
    return particles

def update_particle_positions(particles, time_step):
    for particle in particles[1:]:
        particle['position'] += np.random.normal(0.0, 1.0) * time_step

def check_collision(particles, collision_threshold):
    for particle in particles[1:]:
        if abs(particle['position'] - particles[0]['position']) < collision_threshold:
            return True 
    return False

def simulate_first_passage_time(num_particles, box_size, time_step, collision_threshold):
    particles = initialize_particles(num_particles, box_size)
    time_elapsed = 0.0
    
    while not check_collision(particles, collision_threshold):
        update_particle_positions(particles, time_step)
        time_elapsed += time_step
    
    return time_elapsed

# Simulation parameters
num_particles = 5
box_size = 10.0
time_step = 0.1
collision_threshold = 0.1
num_iterations = 100

# Run the simulation for multiple iterations
first_passage_times = []

for _ in range(num_iterations):
    first_passage_time = simulate_first_passage_time(num_particles, box_size, time_step, collision_threshold)
    first_passage_times.append(first_passage_time)

# Calculate and print the average first passage time
average_first_passage_time = np.mean(first_passage_times)
print(f"Average First Passage Time over {num_iterations} iterations: {average_first_passage_time}")

plt.plot(range(1, num_iterations + 1), first_passage_times, marker='o', markeredgecolor = 'red', markerfacecolor='red', linestyle = '-', color='blue')
plt.xlabel('Iteration' , fontsize=12)
plt.ylabel('First Passage Time' , fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gcf().set_size_inches(8,6)
plt.text(0.8, 0.9 , '1 receptor system', horizontalalignment='center', verticalalignment='center', transform = plt.gca().transAxes, fontsize=12, color= 'black')
plt.grid()
plt.show()