import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('materials_database.csv')

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Color map by category
colors = {
    'Metal': '#3498db',
    'Superalloy': '#e74c3c', 
    'Composite': '#2ecc71',
    'Ceramic': '#f39c12'
}

# Plot each material
for idx, row in df.iterrows():
    color = colors.get(row['Category'], '#95a5a6')
    ax.scatter(row['Density_g_cm3'], row['YoungsModulus_GPa'], 
               c=color, s=100, alpha=0.7, edgecolors='white', linewidth=0.5)
    ax.annotate(row['Material'], 
                (row['Density_g_cm3'], row['YoungsModulus_GPa']),
                fontsize=7, alpha=0.8)

# Labels and formatting
ax.set_xlabel('Density, ρ (g/cm³)', fontsize=12)
ax.set_ylabel("Young's Modulus, E (GPa)", fontsize=12)
ax.set_title('Ashby Plot: Young\'s Modulus vs. Density\n(Aerospace Material Selection)', fontsize=14)
ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

# Legend
for cat, col in colors.items():
    ax.scatter([], [], c=col, label=cat, s=80)
ax.legend(loc='upper left', title='Material Family')

plt.tight_layout()
plt.savefig('ashby_plot_modulus_density.png', dpi=200)
plt.show()

print("Plot saved!")

# Now filter for aerospace wing spar criteria
print("\n=== WING SPAR CANDIDATES ===")
print("Criteria: E > 50 GPa, ρ < 3.0 g/cm³, temp > 100°C")
candidates = df[(df['YoungsModulus_GPa'] > 50) & 
                (df['Density_g_cm3'] < 3.0) & 
                (df['MaxServiceTemp_C'] > 100)]
print(candidates[['Material', 'Density_g_cm3', 'YoungsModulus_GPa', 'MaxServiceTemp_C']])