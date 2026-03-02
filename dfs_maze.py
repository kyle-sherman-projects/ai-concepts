import matplotlib.pyplot as plt

# Define the maze as a 7x7 grid.
# 0 = open path (the robot can traverse), 1 = wall (blocked cell).
# The maze is represented as a list of rows, where maze[row][col]
# gives the cell value at that position.
maze = [
    [1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 1]
]

# Start and goal positions expressed as (row, col) tuples.
# start = bottom-left area of the maze, goal = top-right corner.
start = (6, 0)
goal = (0, 6)

# The four cardinal movement directions as (delta_row, delta_col) offsets.
# Right: col+1, Down: row+1, Left: col-1, Up: row-1.
# DFS explores these neighbors in order, but because it uses a LIFO stack
# the last-appended neighbor is visited first.
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs_shortest_path(maze, start, goal):
    """Find a path using Depth-First Search (DFS).

    DFS works by always expanding the most recently discovered node first.
    It uses a LIFO (Last-In, First-Out) stack rather than a FIFO queue
    (which would give BFS). This means DFS dives deep along one branch
    before backtracking to try other branches.

    Note: DFS is NOT guaranteed to find the shortest path. It finds *a*
    valid path if one exists, but that path may be longer than optimal.
    """

    # --- Frontier (the stack) ---
    # Each entry on the stack is a tuple: (current_position, path_so_far).
    # - current_position: (row, col) of the node being considered.
    # - path_so_far: ordered list of (row, col) positions from start
    #   to current_position, used to reconstruct the route when the goal
    #   is reached.
    # We seed the stack with the start node and a path containing only start.
    stack = [(start, [start])]

    # --- Explored set ---
    # Keeps track of every node that has already been popped and expanded.
    # Without this, DFS could revisit nodes indefinitely (infinite loops in
    # cyclic graphs / mazes).
    explored = set()

    # --- Main DFS loop ---
    # Continue as long as there are nodes left to explore on the frontier.
    while stack:

        # Pop the top of the stack (LIFO) — this is what makes it DFS.
        # 'current' is the position we are now visiting.
        # 'path' is the sequence of cells taken to reach 'current'.
        current, path = stack.pop()

        # --- Goal test ---
        # If we've reached the goal, return the path that led here.
        # DFS returns the first complete path it discovers, not necessarily
        # the shortest one.
        if current == goal:
            return path

        # --- Duplicate check ---
        # Only expand this node if we haven't visited it before.
        # A node can appear on the stack multiple times (via different
        # paths), so we skip it if it was already processed.
        if current not in explored:
            explored.add(current)

            # --- Expand neighbors ---
            # Try each of the four movement directions in order.
            for dr, dc in directions:
                nr, nc = current[0] + dr, current[1] + dc

                # Validity checks before adding a neighbor to the stack:
                #   1. Stay within the grid boundaries.
                #   2. The cell must be an open path (maze value == 0).
                #   3. The cell must not already be in the explored set
                #      (avoids pushing obviously redundant states).
                if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
                        maze[nr][nc] == 0 and (nr, nc) not in explored):

                    # Push the neighbor onto the stack with the updated path.
                    # path + [(nr, nc)] creates a new list (immutable snapshot)
                    # so that different branches on the stack don't share the
                    # same path object.
                    stack.append(((nr, nc), path + [(nr, nc)]))

    # If the stack is exhausted with no path found, return None.
    return None


def plot_maze(maze, path, start, goal):
    """Visualize the maze and the path found by DFS."""
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw the maze grid: paint each wall cell black.
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                ax.add_patch(plt.Rectangle((c, rows - r - 1), 0.97, 0.97, color='black'))

    # Highlight the DFS path with red arrows connecting consecutive cells.
    if path:
        for i in range(len(path) - 1):
            x1, y1 = path[i][1] + 0.5, rows - path[i][0] - 0.5
            x2, y2 = path[i + 1][1] + 0.5, rows - path[i + 1][0] - 0.5
            ax.arrow(x1, y1, x2 - x1, y2 - y1,
                     head_width=0.12, length_includes_head=True,
                     head_length=0.12, fc='red', ec='red')

    # Mark start state in green and goal state in blue.
    ax.add_patch(plt.Rectangle((start[1] + 0.25, rows - start[0] - 1 + 0.25), 0.5, 0.5, color='green'))
    ax.add_patch(plt.Rectangle((goal[1] + 0.25, rows - goal[0] - 1 + 0.25), 0.5, 0.5, color='blue'))

    # Formatting
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Robot Maze Navigation - Shortest Path")
    plt.show()


# Solve the maze using DFS. dfs_path will be a list of (row, col) tuples
# representing the route from start to goal, or None if no path exists.
dfs_path = dfs_shortest_path(maze, start, goal)

# Visualize the maze and overlay the DFS path.
plot_maze(maze, dfs_path, start, goal)
