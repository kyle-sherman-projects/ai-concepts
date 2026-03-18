# For AI680 / CS666 students only

import matplotlib.pyplot as plt
from collections import deque

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
# Right: col+1 | Down: row+1 | Left: col-1 | Up: row-1.
# BFS tries neighbors in this exact order, but the FIFO queue ensures that
# ALL nodes at depth d are fully explored before any node at depth d+1,
# which is what guarantees the shortest path.
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs_shortest_path(maze, start, goal):
    """Find the shortest path through the maze using Breadth-First Search (BFS).

    BFS works by expanding nodes level by level, where a "level" corresponds
    to the number of steps taken from the start position.  It uses a FIFO
    (First-In, First-Out) queue, so the node that has been waiting the longest
    is always processed next.  This guarantees that the first time BFS reaches
    the goal it has taken the fewest possible steps — i.e. the path is optimal.

    Key difference vs DFS:
        DFS uses a LIFO stack  → dives deep along one branch before backtracking
        BFS uses a FIFO queue  → fans out uniformly in all directions

    Args:
        maze  : 2-D list of ints  (0 = open, 1 = wall)
        start : (row, col) tuple  — starting cell
        goal  : (row, col) tuple  — destination cell

    Returns:
        A list of (row, col) tuples representing the shortest path from start
        to goal (inclusive), or None if no path exists.
    """

    # --- Frontier (the queue) ---
    # deque (double-ended queue) from the 'collections' module is used instead
    # of a plain list because popleft() runs in O(1) time.  Removing from the
    # front of a plain Python list is O(n) — prohibitively slow for large mazes.
    #
    # Each entry in the queue is a two-element tuple:
    #   (current_position, path_so_far)
    #   - current_position : (row, col) of the cell being considered right now.
    #   - path_so_far      : ordered list of (row, col) cells from start up to
    #                        and including current_position.  We carry the full
    #                        path in every queue entry so we can reconstruct the
    #                        route without needing a separate "parent" map.
    #
    # We seed the queue with the start node; the path contains only start.
    queue = deque([(start, [start])])

    # --- Explored set ---
    # A Python set of every cell that has already been dequeued and expanded.
    # Sets provide O(1) average-case membership tests, which keeps BFS fast.
    #
    # Why we need this:
    #   The maze is a cyclic graph — cells connect to each other in loops.
    #   Without tracking visited cells BFS would enqueue the same cell multiple
    #   times and loop forever.  Once a cell is explored at depth d we never
    #   need to visit it again: BFS already found the shortest route to it.
    explored = set()

    # --- Main BFS loop ---
    # Continue as long as there are nodes left to explore on the frontier.
    # If the queue empties without finding the goal, the maze has no solution.
    while queue:

        # Dequeue from the LEFT (FIFO) — this is what makes it BFS.
        # The cell with the smallest number of steps from start is always
        # processed first, enforcing the level-by-level expansion order.
        current, path = queue.popleft()

        # --- Goal test ---
        # Check whether the cell we just dequeued is the destination.
        # Because BFS expands nodes in order of increasing path length, the
        # very first time we dequeue the goal cell we are guaranteed that
        # 'path' is one of the shortest possible routes — return it immediately.
        if current == goal:
            return path

        # --- Duplicate / already-explored check ---
        # A cell can be enqueued more than once (via different paths of equal
        # length) before it is ever dequeued.  We only want to expand it once;
        # skip it if it was already processed on a previous iteration.
        if current not in explored:

            # Mark this cell as explored so we never expand it again.
            explored.add(current)

            # --- Expand neighbors ---
            # Try each of the four movement directions in order.
            for dr, dc in directions:
                # Compute the (row, col) of the neighbor in direction (dr, dc).
                nr, nc = current[0] + dr, current[1] + dc

                # Validity checks before enqueuing the neighbor:
                #   1. Stay within the grid boundaries (avoid IndexError).
                #   2. The cell must be an open path (maze value == 0, not a wall).
                #   3. The cell must not already be in the explored set;
                #      adding already-explored cells would waste queue space
                #      without ever changing the answer.
                if (0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and
                        maze[nr][nc] == 0 and (nr, nc) not in explored):

                    # Enqueue the neighbor at the RIGHT end of the deque (FIFO).
                    # path + [(nr, nc)] builds a NEW list that extends the
                    # current path by one cell.  Each queue entry gets its own
                    # independent list so that branching paths do not interfere
                    # with one another — this is important because multiple
                    # neighbors may be enqueued from the same parent cell.
                    queue.append(((nr, nc), path + [(nr, nc)]))

    # The queue is empty and we never reached the goal.
    # This means no path exists between start and goal in this maze.
    return None


def plot_maze(maze, path, start, goal):
    """Visualize the maze and the shortest path found by BFS."""
    rows, cols = len(maze), len(maze[0])
    fig, ax = plt.subplots(figsize=(6, 6))

    # Draw the maze grid: paint each wall cell (value == 1) solid black.
    # Open cells (value == 0) are left as the default white background.
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                ax.add_patch(plt.Rectangle((c, rows - r - 1), 0.97, 0.97, color='black'))

    # Highlight the BFS shortest path with red arrows.
    # We iterate over consecutive pairs of cells in the path and draw an
    # arrow from each cell's centre to the next cell's centre.
    #
    # Coordinate conversion — maze (row, col) → plot (x, y):
    #   x = col + 0.5   (shift to cell centre horizontally)
    #   y = rows - row - 0.5   (flip vertically: row 0 is at the top of the
    #                            maze but at the TOP of the y-axis in the plot)
    if path:
        for i in range(len(path) - 1):
            x1, y1 = path[i][1] + 0.5,     rows - path[i][0] - 0.5
            x2, y2 = path[i + 1][1] + 0.5, rows - path[i + 1][0] - 0.5
            # ax.arrow draws from (x1,y1) by a delta (dx, dy).
            # length_includes_head=True keeps the total arrow length correct.
            ax.arrow(x1, y1, x2 - x1, y2 - y1,
                     head_width=0.12, length_includes_head=True,
                     head_length=0.12, fc='red', ec='red')

    # Mark the start cell with a green square and the goal cell with a blue square.
    # The offset of +0.25 and size of 0.5 centres a small marker inside the cell.
    ax.add_patch(plt.Rectangle((start[1] + 0.25, rows - start[0] - 1 + 0.25), 0.5, 0.5, color='green'))
    ax.add_patch(plt.Rectangle((goal[1] + 0.25,  rows - goal[0] - 1 + 0.25),  0.5, 0.5, color='blue'))

    # Formatting — remove tick marks and add a descriptive title.
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Robot Maze Navigation - Shortest Path")
    plt.show()


# --- Entry point ---

# Run BFS to find the shortest path from start to goal.
# shortest_path will be a list of (row, col) tuples if a path exists,
# or None if the maze is unsolvable.
shortest_path = bfs_shortest_path(maze, start, goal)

# Render the maze with the solved path overlaid.
plot_maze(maze, shortest_path, start, goal)
