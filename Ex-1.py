import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
file_path = 'resistors.csv'
data = pd.read_csv(file_path)

# Calculate resistor ranges and labels
gaps = np.arange(9400, 10601, 50)
labels = [f"{gaps[i]}-{gaps[i+1]}" for i in range(len(gaps)-1)]
data['Range'] = pd.cut(data['Value'], bins=gaps, labels=labels, right=False)

# Compute statistics
range_counts = data['Range'].value_counts().sort_index()
tolerance1 = data['Value'].between(9900, 10100).sum()
mean = data['Value'].mean()

# Print statistics
print(f"Count of resistors with 1% tolerance: {tolerance1}")
print(f"Mean value of resistors: {mean}")

# Plotting
plt.figure(figsize=(12, 6))
plt.hist(data['Value'], bins=gaps, color='skyblue', edgecolor='black', linewidth=0.5)
plt.title('Resistor Count vs. Range', fontsize=16)
plt.xlabel('Value (Kilo Ohms)', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(ticks=gaps, labels=[f"{gap/1000}" for gap in gaps], rotation=45, fontsize=10)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
