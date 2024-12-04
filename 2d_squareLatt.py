import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 500
P = 700
max_steps = 5000
targets = [(30, 30), (50, 50), (70, 70), (120, 120), (150, 150), (170, 170), (210, 210), (250, 250), (270, 270), (300, 300), (350, 350)]

# Initialize the arrays
first_passage_times = np.full(P, max_steps)
boundary_hits = np.zeros(max_steps + 1)
absorbed = np.zeros(P, dtype=bool)
positions = np.random.randint(0, N, size=(P,2))

for i in range(P):
    (x, y) = positions[i]   # Initialize the position of the particle

    for t in range(1, max_steps + 1):
        dx, dy = np.random.choice([-1, 0, 1], size=2)
        # Update the position of the particle with periodic boundary conditions
        x = (x + dx + N) % N
        y = (y + dy + N) % N

        if x == 0 or x == N-1 or y == 0 or y == N-1:
            boundary_hits[t] += 1
            first_passage_times[i] = t
            break

        if (x, y) in targets:
            absorbed[i] = True
            first_passage_times[i] = t
            break

avg_first_passage_time = np.mean(first_passage_times[~absorbed])
absorbed_fraction = np.sum(absorbed) / P

# Plot
plt.hist(first_passage_times[~absorbed], bins=30, color='blue', alpha=0.7, label='boundary hits', log='True')
plt.hist(first_passage_times[absorbed], bins=30, color='red', alpha=0.7, label='absorbed', log='True')
plt.xlabel('First Passage Time')
plt.ylabel('Frequency')
plt.title('Distribution of First Passage Time')

plt.legend()
plt.show()
print("Average first passage time based on boundary hits only:", avg_first_passage_time)
print("Fraction of particles absorbed by target sites: ", absorbed_fraction)