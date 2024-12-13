class Node:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

def misplaced_tiles(state, goal):
    """Heuristic: Counts the number of tiles that are not in their goal position."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    """Returns a list of possible moves and resulting states."""
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    directions = {
        'Up': (-1, 0),
        'Down': (1, 0),
        'Left': (0, -1),
        'Right': (0, 1)
    }

    for move, (dr, dc) in directions.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            neighbors.append((new_state, move))

    return neighbors

def a_star(initial, goal):
    """A* algorithm using the misplaced tiles heuristic, without using heapq."""
    frontier = [Node(initial, None, None, 0, misplaced_tiles(initial, goal))]
    explored = set()

    while frontier:
        # Find the node with the lowest cost
        frontier.sort(key=lambda node: node.cost)
        node = frontier.pop(0)

        if node.state == goal:
            return reconstruct_path(node)

        explored.add(tuple(node.state))

        for neighbor_state, move in get_neighbors(node.state):
            neighbor = Node(neighbor_state, node, move, node.depth + 1, node.depth + 1 + misplaced_tiles(neighbor_state, goal))

            if tuple(neighbor.state) not in explored:
                frontier.append(neighbor)

    return None

def reconstruct_path(node):
    """Reconstructs the path to the solution."""
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]

def input_state(prompt):
    """Helper function to input a state from the user."""
    print(prompt)
    state = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (3 numbers separated by spaces, 0 for the empty space): ").split()
        state.extend(int(x) for x in row)
    return state

# Example usage with user input:
initial_state = input_state("Enter the initial state:")
goal_state = input_state("Enter the goal state:")

solution = a_star(initial_state, goal_state)

if solution:
    print("Solution found:", solution)
else:
    print("No solution exists.")
