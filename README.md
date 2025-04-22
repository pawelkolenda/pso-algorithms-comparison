# Analysis of Acceleration Coefficients in Particle Swarm Optimization

**Analiza_efektywnosci_wspolczynnikow_przyspieszenia_w_metodach_PSO.pdf** is my master's thesis.

## Abstract

The purpose of this master thesis was to analyze and evaluate the effectiveness of various acceleration coefficients used in particle swarm optimization (PSO) methods. An original group of speed coefficients has been proposed, based on a solution that assumes a change in the coefficient values over time. It was extended by the momentary and cyclical knocking out of particles from their current positions in the initial and final stages of the algorithm run. The purpose of this modification is to minimize the effect of premature convergence. A console research application was created to conduct research on the quality of coefficients and to generate results. To provide as many results as possible, eight model test functions, five PSO methods, and six groups of coefficients were used. More than two hundred experiments were carried out to show the broadest spectrum of the quality of the proposed coefficients.

**Keywords:** particle swarm optimization, PSO, efficiency, coefficients, velocity

## Project Description

This research project implements and compares different variants of Particle Swarm Optimization (PSO) algorithms with a focus on analyzing various acceleration coefficients. The project evaluates the effectiveness of different coefficient configurations across multiple PSO modifications:

- Classic PSO
- PSO with Ring Topology
- PSO with Spatial Neighborhood
- PSO with Star Topology
- PSO with Selection Mechanism

The research includes six different groups of acceleration coefficients, with special attention to time-varying coefficients and mechanisms to prevent premature convergence.

Each algorithm configuration is tested on eight benchmark functions:
- Sphere Function
- F2 Function
- Rosenbrock Function
- Griewank Function
- Rastrigin Function
- Ackley Function
- Schwefel Function
- Zakharov Function

The project includes comprehensive visualization and analysis capabilities to compare the performance of different coefficient configurations across various algorithms and functions.

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
├── coefficient_factory.py    # Coefficient generation and analysis
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
- Coefficient configurations

## Usage

1. Configure the parameters in `config.json` according to your needs.

2. Run the main script:
```bash
python main.py
```

3. The results will be:
   - Exported to Excel files in the `results` directory
   - Visualized using Matplotlib plots
   - Analyzed for coefficient effectiveness

## Results

The project generates comprehensive results including:
- Detailed analysis of coefficient effectiveness across different PSO variants
- Performance comparison of time-varying coefficients
- Evaluation of premature convergence prevention mechanisms
- Statistical analysis of over 200 experiments
- Visual plots comparing the performance of different coefficient configurations
- Average best solutions per iteration for detailed analysis
