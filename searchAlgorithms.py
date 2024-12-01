from objects import Objects
from collections import deque
from typing import List

class SearchAlgorithms:
    def __init__(self, maze: List[List[int]], size: int, start: tuple, goal: tuple) -> None:
        self.maze = maze
        self.size = size
        self.start = start
        self.goal = goal

    def dfs(self):
        pass

    def bfs(self):
        queue = deque([self.start])
        visited = set()
        visited.add(self.start)
        parent = {self.start: None}

        while(queue):
            x, y = queue.popleft()
            if (x, y) == self.goal:
                return self.__get_path(parent)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if((0 <= nx < self.size) and (0 <=ny < self.size) and self.maze[nx][ny] != Objects.WALL.value):
                    if( (nx, ny) not in visited):
                        parent[(nx, ny)] = (x, y)
                        visited.add((nx, ny))
                        if (nx, ny) == self.goal:
                            return self.__get_path(parent)
                        queue.append((nx, ny))
        
        return []

    
    def a_star(self):
        pass
    

    def __get_path(self, parent: dict) -> List:
        path = []
        current = self.goal

        while current is not None:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        return path
        


        