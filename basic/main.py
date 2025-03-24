# proton & neutron swap

def reorder_particles(particles):
    n = len(particles)

    # all protons must appear before neutron
    for i in range(n):
        for j in range(0, n - i - 1):
            print(f"j, first is {i} is a {j}")
            if particles[j] == 'n' and particles[j + 1] == 'p':
                particles[j], particles[j + 1] = particles[j + 1], particles[j]

    return particles

p = ["n", "p", "p", "n", "p", "n"]

print(reorder_particles(p))