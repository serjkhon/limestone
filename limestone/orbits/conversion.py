import numpy as np
from limestone.core.elements import OrbitalElements

def elements_to_state(elements: OrbitalElements, nu: float, mu: float):

# convert orbital elements + true anomaly to state vectors (position, velocity).
# mu : gravitational parameter = G * M, m³/s²
# nu : true anomaly, radians

    a, e, i = elements.a, elements.e, elements.i
    Omega, omega = elements.Omega, elements.omega

    # distance from focus to planet
    r = a * (1 - e**2) / (1 + e * np.cos(nu))

    # position in the flat 2D orbital plane
    x_orb = r * np.cos(nu)
    y_orb = r * np.sin(nu)

    # speed factor
    p = a * (1 - e**2)
    v_factor = np.sqrt(mu / p)

    # velocity in the flat 2D orbital plane
    vx_orb = -v_factor * np.sin(nu)
    vy_orb =  v_factor * (e + np.cos(nu))

    # rotation matrix: orbital plane to 3D space
    cos_O = np.cos(Omega)
    sin_O = np.sin(Omega)
    cos_o = np.cos(omega)
    sin_o = np.sin(omega)
    cos_i = np.cos(i)
    sin_i = np.sin(i)

    # position in 3D space
    x = (cos_O * cos_o - sin_O * sin_o * cos_i) * x_orb + (-cos_O * sin_o - sin_O * cos_o * cos_i) * y_orb
    y = (sin_O * cos_o + cos_O * sin_o * cos_i) * x_orb + (-sin_O * sin_o + cos_O * cos_o * cos_i) * y_orb
    z = (sin_i * sin_o) * x_orb + (sin_i * cos_o) * y_orb

    position = np.array([x, y, z])

    # velocity in 3D space
    vx = (cos_O * cos_o - sin_O * sin_o * cos_i) * vx_orb + (-cos_O * sin_o - sin_O * cos_o * cos_i) * vy_orb
    vy = (sin_O * cos_o + cos_O * sin_o * cos_i) * vx_orb + (-sin_O * sin_o + cos_O * cos_o * cos_i) * vy_orb
    vz = (sin_i * sin_o) * vx_orb + (sin_i * cos_o) * vy_orb

    velocity = np.array([vx, vy, vz])


    return position, velocity