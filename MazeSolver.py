from typing import List
import matplotlib.pyplot as plt
from maze import Maze
from searchAlgorithms import SearchAlgorithms
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.animation import FuncAnimation

def visualise_maze_with_path(maze: List[List[int]], path: List[int], title: str):
    """
    Visualize the maze with animation for the path.

    Args:
        maze (list[list[int]]): A 2D grid representing the maze.
        path (list[tuple[int, int]]): A list of (row, col) tuples representing the path.
    """
     # Define the colormap and boundaries
    cmap = ListedColormap(['white', 'black', 'red', 'green', 'blue', 'yellow'])
    norm = BoundaryNorm([0, 1, 2, 3, 4, 5, 6], cmap.N)

    # Convert maze to a numpy array
    maze = np.array(maze, dtype=int)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    img = ax.imshow(maze, cmap=cmap, norm=norm, interpolation='nearest')

    # Add grid lines
    ax.set_xticks(np.arange(-0.5, maze.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, maze.shape[0], 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
    ax.tick_params(which="minor", size=0)  # Hide tick marks
    ax.set_xticks([])  # Hide major ticks
    ax.set_yticks([])

    ax.set_title(title, fontsize=16, pad=10)

    # Function to update the maze for each frame of the animation
    def update(frame):
        if frame < len(path):
            # Update the path with "green" (value 3 in colormap)
            row, col = path[frame]
            maze[row, col] = 3  # Mark the cell as part of the path
            img.set_array(maze)

    # Create the animation
    anim = FuncAnimation(fig, update, frames=len(path), interval=200, repeat=False)

    plt.show()


if __name__ == "__main__":
    maze = Maze(10)
    maze.generate_maze(wall_probablity=0.3, trap_probablity=0.05)

    search = SearchAlgorithms(maze.get_maze(), maze.get_size(), maze.get_start(), maze.get_goal())
    path = search.bfs()
    if path:
        #print(f"Path found by BFS {path}")
        visualise_maze_with_path(maze.get_maze(), path, f"Solving with BFS. Time taken: {search.get_time_to_solve()}")
    else:
        print("Maze cannot be solved by BFS")
    

    path = search.dfs()
    if path:
        #print(f"Path found by DFS {path}")
         visualise_maze_with_path(maze.get_maze(), path, f"Solving with DFS. Time taken: {search.get_time_to_solve()}")
    else:
        print("Maze cannot be solved by DFS")


