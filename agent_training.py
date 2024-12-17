import numpy as np
import random
from warehouse_visualization import WarehouseVisualization, plot_rewards
from time import sleep
from time import time
from statistics import mean
from environment import Environment

random.seed(42)
np.random.seed(42)

# Initialize Q-table
def initialize_q_table(grid_size):
    return np.zeros((grid_size * grid_size, 5))

# Convert state to index
def state_to_index(position, grid_size):
    x, y = position
    return x * grid_size + y


def move_humans(g,aigent_position, step):
    human_positions = np.argwhere(g == 3).tolist()
    new_positions = []
    if step == 0:
        for pos in human_positions:
            x, y = pos
            g[x, y] = 0 # Clear current human position

            # Choose a random direction to move
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            random.shuffle(moves)
            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_x < g.shape[0] and new_y < g.shape[1] and new_y >= 0 and g[new_x, new_y] == 0 and aigent_position != (new_x, new_y)  :
                    x, y = new_x, new_y
                    break
            g[x, y] = 3  # Move human
            new_positions.append([x, y])

        return new_positions
    else:
        return human_positions
        
# Training loop with visualization
def train_agent(environment,
                q_tables,
                visualizer,
                targets,
                start =(0, 0),
                episodes = 4000,
                max_steps = 300,
                epsilon =1,
                learning_rate = 0.1,
                discount_factor = 0.9,
                epsilon_decay = 0.995,
                min_epsilon = 0.1,
                visualization_range = range(0,100000), # change the range to visualize a range of episodes
                print_done = False):
    
    rewards_per_episode = []  # To store total rewards per episode
    grid = environment.grid
    q_table_num = 0
    current_position = start
    num_targets = len(targets)+1
    for episode in range(episodes):
        grid_copy = grid.copy()
        total_reward = 0
        done = "No"

        #for step in range(max_steps):
        for step in range(max_steps):
            q_table = q_tables[q_table_num%num_targets]
            if done == "No" :

                state = state_to_index(current_position, environment.grid_size)

                if random.uniform(0, 1) < epsilon:
                    action = random.choice(range(5))
                else:
                    action = np.argmax(q_table[state])

                next_position, reward, grid, done = environment.take_step(grid_copy, current_position, action)
                #humans_positions = move_humans(grid_copy,current_position,0)               
                next_state = state_to_index(next_position, environment.grid_size)

                q_table[state, action] += learning_rate * (
                reward + discount_factor * np.max(q_table[next_state]) - q_table[state, action])
    
                current_position = next_position
                total_reward += reward

            elif done == "Returned":
                if print_done:
                    print(done)
                q_table_num +=1
                for target in targets:
                    grid[target]=2
                grid[start]=0
                current_position = start
                break
            elif done == "All":
                if print_done:
                    print(done)
                q_table_num +=1
                grid[start]=4
                break
            elif done == "One":
                q_table_num +=1
                break
            elif done == "Out" or done =="Obstacle" or done =="Human":
                break
            if visualizer!= None and episode in visualization_range:
                visualizer.update_agent_position(next_position,humans_positions,0)  # Update visualization
        epsilon = max(min_epsilon, epsilon * epsilon_decay)
        rewards_per_episode.append(total_reward)  # Store total reward
        #print(f"Episode {episode + 1}, Total Reward: {total_reward}")
    return rewards_per_episode


# Main execution
if __name__ == "__main__":
    #targets = [(3,6),(4,3),(5,5)]
    grid_size = 12
    targets = [(9,3),(8,6),(8,10)]
    humans_positions = [(3, 3),(6, 5)]

    # Parameters
    num_targets = len(targets)
    episodes = 4000  # Reduce for faster visualization
    max_steps = 300  # Max steps per episode
    cell_size = 50  # Size of each cell in the canvas
    epsilon =1
    learning_rate = 0.1 #0.41843066996265676
    discount_factor = 0.9 #0.8598882585746133
    epsilon_decay = 0.995 #0.9850819835498889
    min_epsilon = 0.1   
    visualization_range = range(3990,3999)# change the range to visualize a range of episodes

    environment = Environment(grid_size, targets, humans_positions)

    def run_ex(ex_num=25):

        times = []
        rewards = []
        for i in range(ex_num):
            q_tables = []
            for target in range(num_targets+1):
                q_table = initialize_q_table(grid_size)
                q_tables.append(q_table)
            start_time = time()*1000.0
            rewards_per_episode = train_agent(environment,
                                               q_tables,
                                                 None,
                                                 targets,
                                                 episodes=episodes,
                                                 max_steps=max_steps,
                                                epsilon =epsilon,
                                                learning_rate = learning_rate,
                                                discount_factor = discount_factor,
                                                epsilon_decay = epsilon_decay,
                                                min_epsilon = min_epsilon,
                                                 visualization_range= visualization_range)
            end_time = time()*1000.0
            trainning_time = end_time - start_time
            times.append(trainning_time)
            rewards.append(mean(rewards_per_episode))

        return mean(times), mean(rewards)
    

    q_tables = [initialize_q_table(grid_size) for _ in range(num_targets + 1)]


    visualizer = WarehouseVisualization(environment.grid, cell_size)
    rewards_per_episode =  train_agent(environment,
                                        q_tables,
                                        visualizer,
                                        targets,
                                        episodes=episodes,
                                        max_steps=max_steps,
                                        epsilon =epsilon,
                                        learning_rate = learning_rate,
                                        discount_factor = discount_factor,
                                        epsilon_decay = epsilon_decay,
                                        min_epsilon = min_epsilon,
                                        visualization_range= visualization_range)

    # Visualize the learned optimal policy
    for q_table in q_tables:
        visualizer.visualize_policy(q_table)

        visualizer.root.mainloop(1)
        sleep(5)


    # Plot rewards after training
    plot_rewards(rewards_per_episode)

    ex_time, av_reward = run_ex()
    print("Average time",ex_time)
    print("Average reward",av_reward)    
