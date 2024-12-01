class Maze:
    def __init__(self, size: int) -> None:
        self.size = size
        self.start = (0, 0)
        self.goal = (size-1, size-1)
    
    def set_start(self, start: tuple) -> None:
        self.start = start
    
    def set_goal(self, goal: tuple) -> None:
        self.goal = goal
    
    def get_start(self) -> tuple:
        return self.start
    
    def get_goal(self) -> tuple:
        return self.goal
    

    def generate_maze(self, wall_probablity=0.3, trap_probablity=0.3):
        while True:
            # Creating an empty maze here
            maze = [[0 for _ in range(self.size)] for _ in range(self.size)]


    
        