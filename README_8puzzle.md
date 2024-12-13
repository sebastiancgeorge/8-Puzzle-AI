
# 8 Puzzle Solver

This is a Python implementation of the 8-puzzle problem solver using the A* algorithm. 
The program accepts an initial state and a goal state, then computes the sequence of moves required to solve the puzzle.

## Features
- Implements the A* algorithm with a heuristic based on the number of misplaced tiles.
- Accepts custom input for the initial and goal states.
- Displays the solution as a sequence of moves.

## How to Use

1. Run the script using Python:
   ```bash
   python 8puzz.py
   ```

2. Enter the initial state and the goal state when prompted. Input each row as three numbers separated by spaces, using `0` to represent the empty space.

   Example:
   ```
   Enter the initial state:
   Enter row 1 (3 numbers separated by spaces, 0 for the empty space): 1 2 3
   Enter row 2 (3 numbers separated by spaces, 0 for the empty space): 4 5 6
   Enter row 3 (3 numbers separated by spaces, 0 for the empty space): 7 8 0

   Enter the goal state:
   Enter row 1 (3 numbers separated by spaces, 0 for the empty space): 1 2 3
   Enter row 2 (3 numbers separated by spaces, 0 for the empty space): 4 5 6
   Enter row 3 (3 numbers separated by spaces, 0 for the empty space): 0 7 8
   ```

3. The program will compute the solution and display the sequence of moves.

   Example output:
   ```
   Solution found: ['Left', 'Down', 'Right']
   ```

## Functions

- **Node Class**: Represents a state in the search tree.
- **misplaced_tiles(state, goal)**: Heuristic function that counts the number of tiles not in their goal position.
- **get_neighbors(state)**: Generates all valid moves and resulting states.
- **a_star(initial, goal)**: Solves the 8-puzzle using the A* algorithm.
- **reconstruct_path(node)**: Reconstructs the sequence of moves from the solution node.

## Dependencies

- Python 3.x

## Notes

- The heuristic used is admissible, ensuring the optimal solution.
- If no solution exists, the program will display `No solution exists.`

Feel free to modify and extend the script to include additional heuristics or GUI-based input.

## License

This code is provided under the MIT License. You are free to use, modify, and distribute it as needed.
