# AI-MAZE-Solver

## Overview
This project implements and compares multiple Artificial Intelligence (AI) search algorithms for solving maze navigation problems.

The program loads a maze from a text file, applies different search algorithms, and displays:
- Explored nodes
- Final solution path
- Performance statistics (path length, nodes explored, runtime)

This project demonstrates how different AI search strategies behave when solving the same problem.

---

## Algorithms Used
- Breadth-First Search (BFS)
- Greedy Best-First Search
- A* Search

---

## Features
- Load mazes from text files
- Visual display of explored nodes and final path
- Comparison of algorithm performance
- Supports multiple maze configurations
- Handles both solvable and unsolvable mazes

---

## Requirements
- Python 3.x

(No additional libraries are required)

---

## How to Run

1. Download or clone this repository
2. Open the project in VSCode (or any Python IDE)
3. Open a terminal in the project folder
4. Run the program:

```
python main.py
```

5. Select a maze from the list when prompted

---

## Maze Format

Each maze is stored as a `.txt` file using the following symbols:

- `#` = Wall  
- ` ` (space) = Open path  
- `S` = Start position  
- `E` = End position  

### Example Maze
```
#########
#S     E#
#########
```

---

## Project Structure

```
main.py               # Entry point of the program
maze.py               # Maze loading and validation
solver.py             # Search algorithms (BFS, Greedy, A*)
terminalOutput.py     # Terminal-based visualization and output
mazes/                # Folder containing maze text files
```

---

## How It Works

1. The user selects a maze from the available options
2. The program loads and validates the maze
3. Each algorithm (BFS, Greedy, A*) runs on the same maze
4. The program displays:
   - Explored nodes
   - Final path
   - Performance statistics
5. A comparison summary is printed showing differences between algorithms

---

## Authors
- Connor Fletcher
- Stell Hyatt
- Ryan Miller
