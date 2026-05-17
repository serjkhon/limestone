import numpy as np
from limestone.core.elements import OrbitalElements
from limestone.orbits.kepler import solve_kepler, true_anomaly_from_eccentric
from limestone.orbits.conversion import elements_to_state

def propagate(elements: OrbitalElements, t: float, mu: float):
    """
    Given orbital elements and a time t (seconds), return position and velocity.
    t=0 corresponds to the epoch where M = M0.
    """
    n = np.sqrt(mu / elements.a**3)
    M = elements.M0 + n * t
    E = solve_kepler(M, elements.e)
    nu = true_anomaly_from_eccentric(E, elements.e)
    return elements_to_state(elements, nu, mu)