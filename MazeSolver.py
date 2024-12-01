from typing import List
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from maze import Maze

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
    maze.generate_maze()
    visualize_maze(maze.get_maze())

