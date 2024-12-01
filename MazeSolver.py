from typing import List
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from maze import Maze
from searchAlgorithms import SearchAlgorithms

def visualize_maze(maze: List[List[int]]):
    cmap = ListedColormap(['white', 'black', 'red'])

    # Plot the maze
    plt.figure(figsize=(6, 6))
    plt.imshow(maze, cmap=cmap, interpolation='nearest')

    # Add grid lines
    size = len(maze)
    plt.grid(color='gray', linestyle='-', linewidth=0.5)
    plt.xticks(ticks=range(size), labels=[])
    plt.yticks(ticks=range(size), labels=[])
    plt.gca().set_xticks([x - 0.5 for x in range(1, size)], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, size)], minor=True)
    plt.gca().tick_params(axis='both', which='both', length=0)  # Remove tick marks
    plt.gca().grid(True, which='minor', color='black', linewidth=0.7)  # Minor gridlines for maze cells

    plt.title("Maze Visualization with Grid Lines")
    plt.show()


if __name__ == "__main__":
    maze = Maze(10)
    maze.generate_maze(wall_probablity=0.3, trap_probablity=0.05)
    visualize_maze(maze.get_maze())

    search = SearchAlgorithms(maze.get_maze(), maze.get_size(), maze.get_start(), maze.get_goal())
    path = search.bfs()
    if path:
        print(f"Path found {path}")
        print(f"Time taken to solve {search.get_time_to_solve()}")
    else:
        print("Maze cannot be solved")


