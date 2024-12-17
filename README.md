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

## Project Structure

```bash
.
├── main.py                # Main script to run the project
├── requirements.txt       # List of required Python libraries
├── README.md              # Project documentation
└── assets/                # (Optional) Additional resources
