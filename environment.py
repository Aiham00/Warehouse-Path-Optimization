import numpy as np

class Environment:
    def __init__(self, grid_size, targets, humans_positions,start=(0,0)):
        self.grid_size = grid_size
        self.targets = targets
        self.humans_positions = humans_positions
        self.grid = self._create_grid()
        self.start=start

    def _create_grid(self):
        grid = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])

        for target in self.targets:
            grid[target] = 2
        for human_position in self.humans_positions:
            grid[human_position] = 3

        return grid

    def take_step(self,grid, current_position, action):       
        rows, cols = grid.shape
        x, y = current_position
        moves = {
            0: (-1, 0),  # Up
            1: (1, 0),   # Down
            2: (0, -1),  # Left
            3: (0, 1),    # Right
            4: (0, 0)     #Wait
        }
        dx, dy = moves[action]
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
            return (x, y), -300, grid, "Out"  # Out of bounds

        cell_value = grid[new_x, new_y]
        position = (new_x, new_y)

        if cell_value == 1:
            return (x, y), -200, grid, "Obstacle"  # Obstacle 
        elif cell_value == 3:  # Human
            return (x, y), -500, grid, "Human"  # Collision with human
        elif cell_value == 2:
            grid[new_x, new_y] = 0  # Remove item after collection
            all_items_collected = np.count_nonzero(grid == 2) == 0
            if all_items_collected:
                reward = 500  
                return position, reward, grid, "All"

            else:
                reward = 200  # First-time reward
                grid[new_x, new_y] = 0

                return position, reward, grid, "One"
        elif cell_value == 4:
            grid[new_x, new_y] = 0 
            reward = 700  
            return position, reward, grid, "Returned"
        else:
            return position, -1, grid, "No"  # Step penalty for empty space

