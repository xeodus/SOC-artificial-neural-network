import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("activation_results.csv")
print("Columns in DataFrame:", df.columns)
sns.set_theme(style='whitegrid')
plt.figure(figsize=(8,6))
sns.lineplot(
    x='system size',
    y='activated node percentage',
    data=df,
    markers='o',
    color='royalblue',
    linewidth=2,
    label='Average Activation Percentage'
)

plt.xlabel('System Size', fontsize=8)
plt.ylabel('Activated Node Percentage (%)', fontsize=8)
plt.title('Activated Nodes % vs System Size', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend(loc='best', frameon=True, shadow=True, fontsize=8)

plt.show()