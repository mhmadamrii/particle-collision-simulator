import time
import random

def bubble_sort_quantum(particles):
    n = len(particles)
    entropy = sum(abs(particles[i] - particles[i+1]) for i in range(n-1))  # Disorder measure
    
    print(f"\n🔬 Quantum Sorting Initialized: Entropy = {entropy}\n")
    
    for cycle in range(n):
        collision_occurred = False  # Track whether swaps (collisions) happened
        print(f"🌌 Cycle {cycle+1}: Particle interactions begin...\n")
        
        for i in range(n - 1 - cycle):
            print(f"⚛️ Checking particles {particles[i]} and {particles[i+1]}... ", end="")
            
            if particles[i] > particles[i + 1]:
                print("💥 Collision! Momentum exchanged.")
                particles[i], particles[i + 1] = particles[i + 1], particles[i]
                collision_occurred = True
            else:
                print("✔️ Stable configuration.")

            time.sleep(0.1)  # Simulate processing time

        new_entropy = sum(abs(particles[i] - particles[i+1]) for i in range(n-1))
        print(f"\n🌀 Entropy after cycle {cycle+1}: {new_entropy}")

        if not collision_occurred:
            print("\n✅ Quantum equilibrium reached! Sorting complete.\n")
            break

    return particles

particles = [random.randint(1, 100) for _ in range(10)]
print("Initial Particle States:", particles)
sorted_particles = bubble_sort_quantum(particles)
print("Final Particle States (Sorted):", sorted_particles)
