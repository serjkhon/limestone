import numpy as np

def solve_kepler(M: float, e: float, tol: float = 1e-10, max_iter: int = 100) -> float:

# solving Kepler's equation M = E - e*sin(E) for eccentric anomaly E.
# uses Newton-Raphson iteration.
    E = M + e * np.sin(M)

    for _ in range(max_iter):
        dE = (M - E + e * np.sin(E)) / (1 - e * np.cos(E)) # this part I used as a given
        E += dE
        if abs(dE) < tol:
            return E

    raise RuntimeError(f"Kepler solver did not converge: M={M}, e={e}")

def true_anomaly_from_eccentric(E: float, e: float) -> float:

# converts eccentric anomaly E to true anomaly nu.

    return 2 * np.arctan2(
        np.sqrt(1 + e) * np.sin(E / 2),
        np.sqrt(1 - e) * np.cos(E / 2)
    )