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

def plot_nbody(history: np.ndarray, labels: list = None):
    """
    Plot trajectories from an n-body simulation.
    history : (n_steps, N, 3) array from leapfrog
    labels  : list of names for each body
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    N = history.shape[1]

    for i in range(N):
        x = history[:, i, 0]
        y = history[:, i, 1]
        z = history[:, i, 2]
        label = labels[i] if labels else f"body {i}"
        ax.plot(x, y, z, label=label)
        ax.scatter(x[0], y[0], z[0], s=50)

    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.legend()
    plt.show()

def plot_lidov_kozai(solution):
    """
    Plot eccentricity and inclination evolution from a Lidov-Kozai integration.
    """
    t = solution.t
    e = solution.y[0]
    i = np.degrees(solution.y[1])

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.plot(t, e)
    ax1.set_ylabel('Eccentricity')
    ax1.set_title('Lidov-Kozai Oscillations')

    ax2.plot(t, i, color='orange')
    ax2.set_ylabel('Inclination (degrees)')
    ax2.set_xlabel('Time (s)')

    plt.tight_layout()
    plt.show()