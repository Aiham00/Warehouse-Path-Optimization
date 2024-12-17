import tkinter as tk
import numpy as np
import random
random.seed(42)
np.random.seed(42)
import matplotlib.pyplot as plt

# Convert state to index
def state_to_index(position, grid_size):
    x, y = position
    return x * grid_size + y

# Visualization class
class WarehouseVisualization:
    def __init__(self, grid, cell_size):
        self.grid = grid
        self.grid_size = len(grid)
        self.cell_size = cell_size
        self.agent_position = (0, 0)
        self.humans_positions = np.argwhere(self.grid == 3).tolist()
        self.root = tk.Tk()
        self.root.title("Warehouse Robot Path Optimization")
        self.canvas = tk.Canvas(self.root, width=self.grid_size * cell_size, height=self.grid_size * cell_size)
        self.canvas.pack()
        
        self.render_grid()

    def render_grid(self):
        self.canvas.delete("all")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                if self.grid[i, j] == 1:  # Obstacle
                    color = "black"
                elif self.grid[i, j] == 2:  # Item
                    color = "blue"
                elif (i, j) == self.agent_position:  # Agent
                    color = "red"
                elif [i,j] in self.humans_positions :  # Human
                    color = "yellow"
                else:  # Empty space
                    color = "white"
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    def visualize_policy(self, q_table):
        """Visualize the optimal policy on the grid using arrows."""
        self.canvas.delete("all")
        self.render_grid()  # Draw the base grid
        
        arrow_directions = {
            0: (0, -1),   # Up
            1: (0, 1),    # Down
            2: (-1, 0),   # Left
            3: (1, 0),     # Right
            4: (0, 0) 
        }
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                state = state_to_index((i, j), self.grid_size)
                if np.all(q_table[state] == 0):  # Skip states with no learned values
                    continue
                
                # Find the best action for the current state
                best_action = np.argmax(q_table[state])
                dx, dy = arrow_directions[best_action]
                
                # Draw arrow for the best action
                x1 = j * self.cell_size + self.cell_size // 2
                y1 = i * self.cell_size + self.cell_size // 2
                x2 = x1 + dx * self.cell_size // 3
                y2 = y1 + dy * self.cell_size // 3
                
                self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="green", width=2)
        
        self.root.update()
    def update_agent_position(self, position,humans_positions, render_step=10):
        self.agent_position = position
        #self.humans_positions = humans_positions
        if render_step == 1 or render_step % 10 == 0:  # Update every 10th step
            self.render_grid()
            self.root.update()

def plot_rewards(rewards):
    episodes = range(1, len(rewards) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, rewards, label="Total Reward per Episode")
    
    # Calculate and plot moving average
    window_size = 10
    moving_avg = np.convolve(rewards, np.ones(window_size)/window_size, mode='valid')
    plt.plot(episodes[:len(moving_avg)], moving_avg, label=f"{window_size}-Episode Moving Average", linestyle="--")
    
    plt.title("Reward Progression Over Episodes")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.legend()
    plt.grid()
    plt.show()
