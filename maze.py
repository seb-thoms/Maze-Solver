from typing import List
import random
from collections import deque
from objects import Objects

class Maze:
    def __init__(self, size: int) -> None:
        self.size = size
        self.start = (0, 0)
        self.goal = (size-1, size-1)
        self.maze = None
    
    def set_start(self, start: tuple) -> None:
        self.start = start
    
    def set_goal(self, goal: tuple) -> None:
        self.goal = goal
    
    def get_start(self) -> tuple:
        return self.start
    
    def get_goal(self) -> tuple:
        return self.goal
    
    def get_maze(self) -> List[List[int]]:
        return self.maze
    
    def get_size(self) -> int:
        return self.size
    

    def generate_maze(self, wall_probablity: float = 0.3, trap_probablity: float = 0.01) -> None:
        while True:
            # Creating an empty maze here
            self.maze = [[0 for _ in range(self.size)] for _ in range(self.size)]

            # Randomly place walls
            self.__create_obstacles(Objects.WALL.value, wall_probablity)

            # Randomly place traps
            self.__create_obstacles(Objects.TRAP.value, trap_probablity)

            # Ensure start and goal does not have wall or traps
            self.maze[self.start[0]][self.start[1]] = 0
            self.maze[self.goal[0]][self.goal[1]] = 0

            # Need to make sure the maze is valid.
            if self.__is_path_exists():
                break
    

    def __create_obstacles(self, obstacle: Objects, obstacle_probablity: float):
        for i in range(self.size):
            for j in range(self.size):
                if(self.maze[i][j] == 0):
                    if(random.random() < obstacle_probablity):
                        self.maze[i][j] = obstacle
    

    def __is_path_exists(self):
        queue = deque([self.start])
        visited = set()
        visited.add(self.start)

        while(queue):
            x, y = queue.popleft()
            if (x, y) == self.goal:
                return True
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if((0 <= nx < self.size) and (0 <=ny < self.size) and self.maze[nx][ny] != Objects.WALL.value):
                    if( (nx, ny) not in visited):
                        visited.add((nx, ny))
                        if (nx, ny) == self.goal:
                            return True
                        queue.append((nx, ny))
        
        return False

            
            



    
        