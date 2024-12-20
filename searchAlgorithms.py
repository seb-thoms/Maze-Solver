from collections import deque
from typing import List
import time
import heapq

class SearchAlgorithms:
    def __init__(self, maze: List[List[int]], size: int, start: tuple, goal: tuple) -> None:
        self.maze = maze
        self.size = size
        self.start = start
        self.goal = goal
        self.start_time = -1
        self.end_time = -1

    def dfs(self):
        self.start_time = time.time()
        stack = [self.start]
        visited = set()
        visited.add(self.start)
        parent = {self.start: None}

        while(stack):
            x, y = stack.pop()
            if (x, y) == self.goal:
                self.end_time = time.time()
                return self.__get_path(parent)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if((0 <= nx < self.size) and (0 <=ny < self.size) and self.maze[nx][ny] == 0):
                    if( (nx, ny) not in visited):
                        parent[(nx, ny)] = (x, y)
                        stack.append((nx, ny))
                        visited.add((nx, ny))
        
        self.end_time = time.time()
        return []




    def bfs(self) -> List:
        self.start_time = time.time()
        queue = deque([self.start])
        visited = set()
        visited.add(self.start)
        parent = {self.start: None}

        while(queue):
            x, y = queue.popleft()
            if (x, y) == self.goal:
                self.end_time = time.time()
                return self.__get_path(parent)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if((0 <= nx < self.size) and (0 <=ny < self.size) and self.maze[nx][ny] == 0):
                    if( (nx, ny) not in visited):
                        parent[(nx, ny)] = (x, y)
                        visited.add((nx, ny))
                        if (nx, ny) == self.goal:
                            self.end_time = time.time()
                            return self.__get_path(parent)
                        queue.append((nx, ny))
        
        self.end_time = time.time()
        return []
    

    def __manhattan_distance(self, current: int) -> int:
        return abs(current[0] - self.goal[0]) + abs(current[1] - self.goal[1])
    
    def a_star(self) -> List:
        self.start_time = time.time()
        priority_queue = []
        heapq.heappush(priority_queue, (0, self.start))
        visited = set()

        parent = {self.start: None}

        while priority_queue:
            current_priority, current = heapq.heappop(priority_queue)
            x, y = current
            if (current not in visited):
                visited.add(current)
                if current == self.goal:
                    self.end_time = time.time()
                    return self.__get_path(parent)
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if((0 <= nx < self.size) and (0 <=ny < self.size) and self.maze[nx][ny] == 0):
                        if( (nx, ny) not in visited):
                            parent[(nx, ny)] = (x, y)
                            heapq.heappush(priority_queue, (self.__manhattan_distance((nx, ny)), (nx, ny)))


    def get_time_to_solve(self) -> int:
        return self.end_time - self.start_time
    

    def __get_path(self, parent: dict) -> List:
        path = []
        current = self.goal

        while current is not None:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        return path
        


        