# cooling-model
Simulation based on Newton's Law of Cooling.

# Roadmap: Newton's Law Cooling Model

A computational thermal simulation tracking food temperature decay based on Newton's law of cooling, fluid/solid thermodynamics, and parametric container geometries.

---

## 1. Mathematical Modeling & Geometry Engine
- [ ] **Define geometric primitives for containers**
  - [ ] Cylinder (`mug`, `cup`): compute open-top surface area ($A = \pi r^2 + 2\pi rh$) and volume ($V = \pi r^2 h$)
  - [ ] Truncated cone / Frustum (`bowl`, `deep_plate`): compute exposed liquid area, wetted container area, and liquid volume based on fill level
  - [ ] Rectangular prism / Elliptic basin (`baking_pan`, `flat_plate`): calculate thin-layer surface-to-volume ratio ($A/V$)
- [ ] **Dynamic geometry solver**
  - [ ] Implement function to compute fill height and exposed cooling surface given a user-specified food mass or volume
  - [ ] Separate heat-loss boundaries (exposed top to air vs. bottom/sides contacting container wall)

## 2. Physical Properties & Food Mechanics
- [ ] **Parametric property modeling**
  - [ ] Replace static lookups with temperature-dependent or composition-based functions for specific heat capacity ($c_p$) and density ($\rho$)
  - [x] Derive mass dynamically via $m = \rho \cdot V$
- [ ] **Convective heat transfer coefficient ($\alpha$ / $h$) calculation**
  - [ ] Model natural air convection based on dimensionless numbers (Grashof, Prandtl, and Nusselt numbers: $\text{Nu} = f(\text{Gr}, \text{Pr})$)
  - [ ] Model evaporative cooling heat loss for high-water-content items (`tea/coffee`, `soup`)
  - [ ] Account for conduction resistance through the container boundary (thermal transmittance $U$)

## 3. Simulation & Solver Core
- [x] **Newton's Law of Cooling numerical solver**
  - [x] Implement explicit Euler integration for the differential form: $\Delta T = \frac{\alpha \cdot A \cdot (T - T_{\text{env}}) \cdot \Delta t}{m \cdot c_p}$
  - [x] Support discrete time-stepping ($\Delta t = 60.0\,\text{s}$)
  - [ ] Compute time-to-target temperature threshold (e.g., safe eating temperature ~50°C–60°C)
- [ ] **Unit tests & physical validation**
  - [ ] Add sanity tests ensuring positive decay and convergence to ambient temperature without numerical overshoot

## 4. CLI & User Interaction (Phase 1)
- [ ] **Interactive terminal input**
  - [x] Prompt for ambient conditions ($T_{\text{ambient}}$)
  - [ ] Add interactive selection for food type, container geometry, and dimensions/fill amount
  - [x] Input validation (bounds checking for food choice via selection loop)
- [ ] **Terminal reporting & visualization**
  - [ ] Display step-by-step summary: calculated $V$, $A$, effective thermal resistance, and cooling rate constant $k$
  - [ ] Render ASCII/Unicode temperature decay curves or tabular progression output

## 5. GUI & Frontend Architecture (Phase 2)
- [ ] **Core decoupling**
  - [ ] Ensure simulation engine runs completely headless without CLI dependencies
- [ ] **Interactive interface**
  - [ ] Design simple parameter input panels (sliders for temperature, dropdowns for container/food presets)
  - [ ] Embed real-time cooling curve plots (e.g., via Matplotlib in PyQt/Tkinter or a lightweight web dashboard)