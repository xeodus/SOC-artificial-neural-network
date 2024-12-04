import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 200
P = 200
max_steps = 10000
targets = [tuple(np.random.randint(0, N, size=2))]

# Initialize the array to store the first passage times
first_passage_times = np.full(N, max_steps)
absorbed = np.zeros(P, dtype=bool)
boundary_hits = np.zeros(max_steps + 1)
positions = np.random.randint(0, N, size=(P, 2))
# Define a function to get neighbors on a periodic honeycomb lattice
def get_neighbors(x, y, N):
    # Example of neighbors in a hexagonal honeycomb lattice with periodic boundary conditions
    if y % 2 == 0:
        neighbors = [
            ((x - 1) % N, y),  # Left
            ((x + 1) % N, y),  # Right
            (x, (y - 1) % N),  # Down
            (x, (y + 1) % N),  # Up
            ((x - 1) % N, (y - 1) % N),  # Lower Left Diagonal
            ((x + 1) % N, (y + 1) % N)   # Upper Right Diagonal
        ]
    else:
        neighbors = [
            ((x - 1) % N, y),
            ((x + 1) % N, y),
            ((x, (y - 1) % N)),
            ((x, (y + 1) % N)),
            ((x + 1) % N, (y - 1) % N),
            ((x - 1) % N, (y + 1) % N)
        ]   
    return neighbors

for i in range(P):
    (x, y) = positions[i]
    for t in range(1, max_steps + 1):
        (x, y) = get_neighbors(x, y, N)[np.random.randint(6)]

        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            boundary_hits[t] += 1
            first_passage_times[i] = t
            break

        if (x, y) in targets:
            absorbed[i] = True
            first_passage_times[i] = t
            break

# Compute the average first passage time
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