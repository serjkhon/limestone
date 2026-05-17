# limestone

A lightweight Python library for orbital mechanics, built from scratch.

## What it does

- Represent orbits using classical orbital elements
- Solve Kepler's equation numerically
- Convert orbital elements to position and velocity in 3D space
- Propagate orbits forward in time
- Simulate N-body gravitational systems
- Visualize orbits and trajectories in 3D

## Installation

```bash
git clone https://github.com/serjkhon/limestone.git
cd limestone
pip install -e .
```

## Quick start

Plot Earth's orbit:

```python
import numpy as np
from limestone.core.elements import OrbitalElements
from limestone.viz.plot import plot_orbit
import limestone.constants as c

earth = OrbitalElements(a=c.AU, e=0.017, i=0.0, Omega=0.0, omega=0.0, M0=0.0)
plot_orbit(earth, mu=c.G * c.M_SUN)
```

Simulate the Sun, Earth, and Jupiter:

```python
import numpy as np
from limestone.nbody.integrators import leapfrog
from limestone.viz.plot import plot_nbody
import limestone.constants as c

masses = np.array([c.M_SUN, 5.972e24, 1.898e27])

positions = np.array([
    [0.0, 0.0, 0.0],
    [c.AU, 0.0, 0.0],
    [5.2 * c.AU, 0.0, 0.0]
])

velocities = np.array([
    [0.0, 0.0, 0.0],
    [0.0, 29780.0, 0.0],
    [0.0, 13070.0, 0.0]
])

dt = c.YEAR / 365
n_steps = 365 * 5

history = leapfrog(positions, velocities, masses, dt, n_steps)
plot_nbody(history, labels=['Sun', 'Earth', 'Jupiter'])
```

## Dependencies

- numpy
- scipy
- matplotlib

## License

MIT