# Warehouse Robot Path Optimization

This project demonstrates a reinforcement learning approach to optimize the path of a robot navigating through a warehouse grid. The robot avoids obstacles, collects items, and interacts with dynamic human movements while maximizing its rewards. The Q-learning algorithm is used to train the agent, and the training process is visualized using **Tkinter**.

---

## Project Overview

The main objectives of the project include:

- Implementing a Q-learning-based reinforcement learning algorithm.  
- Navigating through a grid-based warehouse environment.  
- Avoiding collisions with obstacles and humans.  
- Collecting all target items in the warehouse.  
- Visualizing the robot's movement and the learned policy in real time.  

---

## Features

### **Grid-Based Environment**
- A customizable warehouse grid with obstacles, humans, and target items.

### **Dynamic Obstacles**
- Humans move randomly, introducing dynamic challenges to the agent's navigation.

### **Visualization**
- The training process is visualized using a GUI (Tkinter).  
- The learned policy can also be displayed using directional arrows.

### **Reward System**
- Designed to incentivize efficient navigation and penalize undesirable actions (e.g., collisions with humans or obstacles).

### **Hyperparameter Optimization**
- Support for hyperparameter tuning using **Optuna**.

---

## Technologies Used

- **Python**  
- **NumPy** - Efficient grid and Q-table computations.  
- **Tkinter** - GUI visualization for agent movement.  
- **Matplotlib** - Plotting the training rewards.  
- **Optuna** - Hyperparameter optimization for Q-learning parameters.  

---

## Installation
- **Clone the repository:**
```bash 
git clone https://github.com/Aiham00/Warehouse-Path-Optimization.git
cd Warehouse-Path-Optimization
```
- **Install the required libraries:**
```bash
pip install -r requirements.txt
```
## How to Run the Project
### Main simulation

To Run the project execute the agent_training Python script:

```bash
python3 agent_training.py
```
### Hyperparameter Tuning
The project integrates Optuna for hyperparameter optimization.

To perform tuning, run hyperparameters_tuning Python script script that uses Optuna to search for the best combination of hyperparameters:
```bash
python3 hyperparameters_tuning.py
```
### What to Expect:
- Watch the robot navigate through the warehouse grid.
- Observe its interactions with the environment, such as avoiding humans and collecting items.
- Visualize rewards and training progression in real time.
### Customization:
Adjust parameters such as **grid size**, **learning rate**, and **epsilon** in the script to customize the training process.

## Key Parameters
The key hyperparameters for training the agent are:

- **grid_size (int): Size of the warehouse grid.**
- **learning_rate (float): Step size for Q-learning updates.**
- **discount_factor (float): Discount factor for future rewards.**
- **epsilon (float): Exploration rate for the ε-greedy policy.**
- **epsilon_decay (float): Decay rate for ε to reduce exploration over time.**
- **episodes (int): Number of training episodes.**
- **max_steps (int): Maximum steps allowed per episode.**

## Dependencies
The required libraries are listed in the requirements.txt file:

```bash

numpy==1.26.4
tk==8.6
matplotlib==3.8.4
optuna==3.6.1
```
Install them with:

```bash
pip install -r requirements.txt
```
---
## Acknowledgments

Inspired by grid-world environments in reinforcement learning.
Optuna framework for hyperparameter optimization.

## Future Improvements
Incorporate more advanced RL algorithms like Deep Q-Learning (DQN).
Add multi-agent cooperation scenarios.
Optimize visualization performance for larger grids.

## Contact
For any questions or suggestions, feel free to reach out:

Name: Ayham Hanna
Email: haay20ju@student.ju.se
Email: aiham682@hotmail.com
GitHub: https://github.com/Aiham00


