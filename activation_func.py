import numpy as np
import pandas as pd

# Parameters
system_size = [1, 3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170]
threshold = 0.7
t_max = 80
dt = 0.1
connection_prob = 0.2
num_trials = 1000
potential_range = [0.0, 1.0]
df = pd.DataFrame(columns=['system size', 'trials', 'activated node percentage'])

# Simulation
for n in system_size:
    trial_results = []
    for trials in range(num_trials):
        potentials = [np.random.uniform(0.0, 1.0) for _ in range(n)]
        
        fired_nodes = [False] * n
        for t in range(0, t_max):
            for i in range(0, n):
                if not fired_nodes[i]:
                    potentials[i] = max(0, min(1, potentials[i] + np.random.uniform(-0.1, 0.1)))
                    if (potentials[i] > threshold):
                        fired_nodes[i] = True

    activated_nodes = sum(1 for fired in fired_nodes if fired)
    percentage_activated = (activated_nodes / n) * 80
    trial_results.append(percentage_activated)
    avg_percentage_activated = sum(trial_results) / len(trial_results)
    
print(f'Percentage of activated nodes for trial {trials + 1} in system size {n}: {percentage_activated:.2f}%')

df = pd.concat([df, pd.DataFrame({'system size': [n], 'trials': [trials], 'activated node percentage': [percentage_activated]})], ignore_index=True)
df.to_csv('activation_results.csv', index=False)
print("Data successfully saved to 'activation_results.csv'")
