import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # <-- This prevents pop-ups, saves to files instead
import matplotlib.pyplot as plt

df = pd.read_csv('materials_database.csv')

colors = {
    'Metal': '#3498db',
    'Superalloy': '#e74c3c', 
    'Composite': '#2ecc71',
    'Ceramic': '#f39c12'
}

def mission_plot(mission_name, x_col, y_col, x_label, y_label, 
                 filter_func, highlight_color, save_name):
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Plot all materials faintly
    for idx, row in df.iterrows():
        color = colors.get(row['Category'], '#95a5a6')
        ax.scatter(row[x_col], row[y_col], c=color, s=80, alpha=0.3)
    
    # Highlight candidates
    candidates = df[filter_func(df)]
    for idx, row in candidates.iterrows():
        ax.scatter(row[x_col], row[y_col], c=highlight_color, 
                   s=200, alpha=0.9, edgecolors='white', linewidth=2)
        ax.annotate(row['Material'], 
                    (row[x_col], row[y_col]),
                    fontsize=8, fontweight='bold')
    
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(f'Mission: {mission_name}', fontsize=14)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3)
    
    for cat, col in colors.items():
        ax.scatter([], [], c=col, label=cat, s=60, alpha=0.3)
    ax.scatter([], [], c=highlight_color, s=120, label='SELECTED', alpha=0.9)
    ax.legend(loc='upper left')
    
    plt.tight_layout()
    plt.savefig(save_name, dpi=200)
    plt.close()  # <-- Close without showing
    
    print(f"\n=== {mission_name.upper()} ===")
    print(candidates[['Material', x_col, y_col, 'MaxServiceTemp_C']])
    return candidates

# Run all 4 missions
print("Generating plots...")

mission_plot("Wing Spar (Stiff vs Light)", 'Density_g_cm3', 'YoungsModulus_GPa',
             'Density (g/cm³)', "Young's Modulus (GPa)",
             lambda d: (d['YoungsModulus_GPa'] > 60) & (d['Density_g_cm3'] < 2.5),
             '#2ecc71', 'mission_wing_spar.png')

mission_plot("Turbine Blade (Strong vs Hot)", 'MaxServiceTemp_C', 'YieldStrength_MPa',
             'Max Temp (°C)', 'Yield Strength (MPa)',
             lambda d: (d['MaxServiceTemp_C'] > 500) & (d['YieldStrength_MPa'] > 500),
             '#e74c3c', 'mission_turbine_blade.png')

mission_plot("Propellant Tank (Strong Metal)", 'Density_g_cm3', 'YieldStrength_MPa',
             'Density (g/cm³)', 'Yield Strength (MPa)',
             lambda d: (d['Category'] == 'Metal') & (d['YieldStrength_MPa'] > 200) & (d['Density_g_cm3'] < 3.0),
             '#3498db', 'mission_propellant_tank.png')

mission_plot("Heat Shield (Hot vs Insulating)", 'ThermalConductivity_W_mK', 'MaxServiceTemp_C',
             'Thermal Conductivity (W/m·K)', 'Max Temp (°C)',
             lambda d: (d['MaxServiceTemp_C'] > 1000) & (d['ThermalConductivity_W_mK'] < 150),
             '#f39c12', 'mission_heat_shield.png')

print("\nAll 4 plots saved! Check your folder.")