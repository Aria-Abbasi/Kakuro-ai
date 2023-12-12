# Kakuro Solver Comparison

## Introduction
This repository contains two implementations of Kakuro puzzle solvers. Kakuro is a logic puzzle that is often described as a mathematical equivalent of the crossword. The first implementation solves the puzzle using a standard backtracking approach, while the second enhances the efficiency by incorporating Most Constrained Variable (MCV) and Least Constraining Value (LCV) heuristics.

The purpose of this repository is to demonstrate the effectiveness of these heuristics in reducing the computational time required to solve Kakuro puzzles.

## Requirements
- Python 3.x
- NumPy library

## Installation
Clone the repository to your local machine:

```
git clone https://github.com/Aria-Abbasi/Kakuro-ai
```

## Usage

### Standard Backtracking Solver
To solve a Kakuro puzzle using the standard backtracking approach:

```python
from kakuro_standard import Kakuro

# Define your puzzle here in a NumPy array format
field = np.array([...])

game = Kakuro(field)
game.solve()
print(game)
```

### MCV and LCV Optimized Solver
To solve a Kakuro puzzle using the MCV and LCV optimized approach:

```python
from kakuro_optimized import Kakuro

# Define your puzzle here in a NumPy array format
field = np.array([...])

game = Kakuro(field)
game.solve()
print(game)
```

## Files in this Repository
- `kakuro_standard.py`: This file contains the Kakuro solver using the standard backtracking approach.
- `kakuro_optimized.py`: This file contains the Kakuro solver enhanced with MCV and LCV heuristics.
- `README.md`: Provides an overview and instructions for this repository.

## Contributing
Feel free to fork this repository and submit pull requests with any optimizations or improvements you devise.
