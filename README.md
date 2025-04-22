# Particle Swarm Optimization (PSO) Algorithms Comparison

This project implements and compares different variants of Particle Swarm Optimization (PSO) algorithms for solving optimization problems. The project evaluates various PSO modifications including different neighborhood topologies and selection mechanisms.

## Project Description

The project implements several PSO variants:
- Classic PSO
- PSO with Ring Topology
- PSO with Spatial Neighborhood
- PSO with Star Topology
- PSO with Selection Mechanism

Each algorithm is tested on multiple benchmark functions:
- Sphere Function
- F2 Function
- Rosenbrock Function
- Griewank Function
- Rastrigin Function
- Ackley Function
- Schwefel Function
- Zakharov Function

The project includes visualization capabilities to compare the performance of different algorithms and functions.

## Technologies Used

- Python 3.x
- NumPy - for numerical computations
- Matplotlib - for result visualization
- Pandas - for data handling and export

## Project Structure

```
.
├── functions/                 # Benchmark functions implementations
├── pso/                      # Classic PSO implementation
├── pso_ring_topology/        # PSO with ring topology
├── pso_spatial_neighborhood/ # PSO with spatial neighborhood
├── pso_star_topology/        # PSO with star topology
├── pso_selection/            # PSO with selection mechanism
├── results/                  # Directory for storing results
├── main.py                   # Main application entry point
├── helper.py                 # Helper functions
├── evaluator.py              # Algorithm evaluation
├── plot_result.py            # Result visualization
├── functions_factory.py      # Benchmark functions factory
├── coefficient_factory.py    # Coefficient generation
├── config.json               # Configuration file
└── clean_results.py          # Results cleanup utility
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Install the required dependencies:
```bash
pip install numpy matplotlib pandas
```

## Configuration

The project can be configured through the `config.json` file, which includes parameters such as:
- Number of dimensions
- Number of particles
- Maximum iterations
- Number of runs
- Number of neighborhoods
- Number of tournament particles

## Usage

1. Configure the parameters in `config.json` according to your needs.

2. Run the main script:
```bash
python main.py
```

3. The results will be:
   - Exported to Excel files in the `results` directory
   - Visualized using Matplotlib plots

## Results

The project generates:
- Excel files with detailed results for each algorithm and function combination
- Visual plots comparing the performance of different algorithms
- Average best solutions per iteration for analysis
