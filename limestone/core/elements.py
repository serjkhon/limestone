from dataclasses import dataclass
import numpy as np

@dataclass
class OrbitalElements:
    a: float      # semi-major axis, meters
    e: float      # eccentricity, dimensionless
    i: float      # inclination, radians
    Omega: float  # longitude of ascending node, radians
    omega: float  # argument of periapsis, radians
    M0: float     # mean anomaly at epoch, radians

    def is_valid(self) -> bool:
        return (
            self.a > 0 and
            0 <= self.e < 1 and
            0 <= self.i <= np.pi
        )