class Particle:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity
        self.energy = 0.5 * mass * velocity ** 2  # Kinetic energy: 1/2 * m * v^2

    def __str__(self):
        return f"Mass: {self.mass}, Velocity: {self.velocity}, Energy: {self.energy}"


def collide(p1, p2):
    v1, m1 = p1.velocity, p1.mass
    v2, m2 = p2.velocity, p2.mass
    p1.velocity = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    p2.velocity = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    p1.energy = 0.5 * p1.mass * p1.velocity ** 2
    p2.energy = 0.5 * p2.mass * p2.velocity ** 2

def sort_particles_by_energy(particles):
    n = len(particles)
    for i in range(n):
        for j in range(0, n - i - 1):
            if particles[j].energy > particles[j + 1].energy:
                particles[j], particles[j + 1] = particles[j + 1], particles[j]
    return particles

if __name__ == "__main__":
    # Create two particles
    particle1 = Particle(mass=2, velocity=5)
    particle2 = Particle(mass=3, velocity=-3)

    print("Before collision:")
    print(particle1)
    print(particle2)

    # Simulate collision
    collide(particle1, particle2)

    print("\nAfter collision:")
    print(particle1)
    print(particle2)

    # Store and sort particles
    particles = [particle1, particle2]
    sorted_particles = sort_particles_by_energy(particles)

    print("\nSorted by energy:")
    for p in sorted_particles:
        print(p)