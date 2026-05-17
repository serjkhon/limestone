import numpy as np
import matplotlib.pyplot as plt
from limestone.core.elements import OrbitalElements
from limestone.orbits.propagator import propagate

def plot_orbit(elements: OrbitalElements, mu: float, n_points: int = 1000):
    """
    Plot a single orbit in 3D space.
    n_points : how many positions to calculate around the orbit
    """
    times = np.linspace(0, 2 * np.pi / np.sqrt(mu / elements.a**3), n_points)

    positions = [propagate(elements, t, mu)[0] for t in times]
    positions = np.array(positions)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
    ax.scatter([0], [0], [0], color='yellow', s=100, label='Star')

    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.legend()

    plt.show()