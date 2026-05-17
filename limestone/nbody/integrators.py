import numpy as np
from limestone.constants import G

def gravitational_acceleration(positions: np.ndarray, masses: np.ndarray) -> np.ndarray:

    # Calculate gravitational acceleration on each body due to all others.
    # positions : (N, 3) array of positions in meters
    # masses    : (N,) array of masses in kg
    # returns   : (N, 3) array of accelerations in m/s²

    N = len(masses)
    accelerations = np.zeros((N, 3))

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            r_vec = positions[j] - positions[i]
            r_mag = np.linalg.norm(r_vec)
            accelerations[i] += G * masses[j] / r_mag**2 * (r_vec / r_mag)
    return accelerations

def leapfrog(positions: np.ndarray, velocities: np.ndarray, masses: np.ndarray, dt: float, n_steps: int):
    """
    Leapfrog integrator for N-body gravitational simulation.
    positions  : (N, 3) array of initial positions in meters
    velocities : (N, 3) array of initial velocities in m/s
    masses     : (N,) array of masses in kg
    dt         : time step in seconds
    n_steps    : number of steps to simulate
    returns    : (n_steps, N, 3) array of positions at each step
    """
    positions = positions.copy()
    velocities = velocities.copy()

    history = np.zeros((n_steps, len(masses), 3))

    acc = gravitational_acceleration(positions, masses)

    for step in range(n_steps):
        positions += velocities * dt + 0.5 * acc * dt**2
        acc_new = gravitational_acceleration(positions, masses)
        velocities += 0.5 * (acc + acc_new) * dt
        acc = acc_new
        history[step] = positions

    return history


    