from particle import Particle

def collide(p1, p2):
    """
    Simulates an elastic collision between two particles in 1D.
    Updates the velocity and energy of both particles.
    """
    v1, m1 = p1.velocity, p1.mass
    v2, m2 = p2.velocity, p2.mass

    # Elastic collision formulas
    p1.velocity = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    p2.velocity = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

    # Update energies after collision
    p1.energy = 0.5 * p1.mass * p1.velocity ** 2
    p2.energy = 0.5 * p2.mass * p2.velocity ** 2