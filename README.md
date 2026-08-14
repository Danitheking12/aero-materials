# Aerospace Materials Selection Engine
### Mission-Driven Ashby Plot Generator

A Python-based computational materials selection tool for aerospace 
component design. Generates Ashby plots — the industry-standard method 
used by Boeing, Rolls-Royce, and NASA for preliminary materials selection.

---

## What This Does

Aerospace components operate under conflicting constraints:

| Component | Primary Need | Secondary Constraint |
|-----------|-------------|---------------------|
| Wing Spar | Stiffness (resist bending) | Minimum weight |
| Turbine Blade | High-temperature strength | Creep resistance |
| Propellant Tank | Pressure containment | Weldability + low mass |
| Heat Shield | Ultra-high temperature | Thermal insulation |

This tool filters a curated materials database across these constraints 
and generates Ashby plots that visualize the optimal material family 
for each mission profile.

---

## Database

14 engineering materials across 4 families:

| Family | Materials | Typical Use |
|--------|-----------|-------------|
| Metals | Al 6061, Al 7075, Ti-6Al-4V, Steel 4340, Be | Structural, tanks |
| Superalloys | Inconel 718, Rene N5 | Turbines, hot sections |
| Composites | CF/Epoxy (0°), CF/Epoxy (quasi), Glass/Epoxy | Wings, fairings |
| Ceramics | SiC, Alumina, ZrB₂ (UHTC) | Heat shields, leading edges |

Properties: Density, Young's Modulus, Yield Strength, Max Service Temp, 
Thermal Conductivity.

---

## Files

| File | Purpose |
|------|---------|
| `materials_database.csv` | Curated property database |
| `ashby_plot.py` | General modulus vs. density plot |
| `mission_selector.py` | Mission-specific filtered plots |
| `mission_wing_spar.png` | Stiffness vs. density (composites highlighted) |
| `mission_turbine_blade.png` | Strength vs. temperature (superalloys highlighted) |
| `mission_propellant_tank.png` | Strength vs. density (metals highlighted) |
| `mission_heat_shield.png` | Temperature vs. conductivity (ceramics highlighted) |

---

## Key Results

**Wing Spar:** Carbon Fiber/Epoxy dominates (E = 150 GPa, ρ = 1.58 g/cm³)  
→ Parallel: Boeing 787 wing box

**Turbine Blade:** Rene N5 selected (σ_y = 900 MPa at 1100°C)  
→ Parallel: GE90 high-pressure turbine

**Propellant Tank:** Ti-6Al-4V optimal (σ_y = 880 MPa, ρ = 4.43 g/cm³)  
→ Parallel: Falcon 9 pressure vessels

**Heat Shield:** ZrB₂ UHTC selected (T_max = 2200°C, κ = 80 W/m·K)  
→ Parallel: Hypersonic leading edges

---

## Validation

This methodology was validated against the author's own failure data: 
a water rocket pressure vessel burst at ~30 psi due to thin-walled PET 
exceeding hoop stress limits. The same selection framework correctly 
predicts that a thicker-walled uniform vessel (Aquafina, t = 0.6 mm) 
survives &gt;80 psi — consistent with hand calculations and FEA results.

---

## Dependencies

```bash
pip install pandas numpy matplotlib
