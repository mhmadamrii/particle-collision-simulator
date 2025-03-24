# Particle Collision Simulator

A Python project that simulates elastic collisions between particles, inspired by particle physics experiments like those in the Large Hadron Collider (LHC). This project uses basic Data Structures and Algorithms (DSA), such as bubble sort, to analyze the results—perfect for beginners looking to blend physics and programming!

## Features

- Simulates 1D elastic collisions between two particles.
- Calculates final velocities and energies using physics formulas.
- Sorts particles by energy with a simple bubble sort algorithm.
- Modular code structure for easy understanding and expansion.

## Why This Project?

As a particle physics enthusiast, I wanted to explore how fundamental interactions work while sharpening my Python and DSA skills. This simulator models a simplified collision scenario and analyzes the outcomes, making it both educational and fun!

## How to Run

1. Clone the repository: `git clone https://github.com/mhmadamrii/particle-collision-simulator.git`
2. Navigate to the project folder: `cd particle-collision-simulator`
3. Install dependencies (if any): `pip install -r requirements.txt`
4. Run the simulation: `python src/main.py`

## Physics Behind It

This project uses the elastic collision formulas for two particles in one dimension:

- `v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)`
- `v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)`
  Where `m1`, `m2` are masses, and `v1`, `v2` are initial velocities.

## Future Ideas

- Add support for multiple particles.
- Visualize collisions with matplotlib.
- Implement more advanced DSA concepts.

## Contributing

Feel free to fork this repo and submit pull requests with improvements or suggestions!
