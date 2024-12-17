import random
import optuna
import numpy as np
from statistics import mean
from environment import Environment
from agent_training import initialize_q_table, train_agent

random.seed(42)
np.random.seed(42)

grid_size = 12
targets = [(9,3),(8,6),(8,10)]
humans_positions = [(3, 3),(6, 5)]
num_targets = len(targets)

environment = Environment(grid_size, targets, humans_positions)


def random_hyperparameters():
    return {
        'learning_rate': random.uniform(0.01, 0.5),
        'discount_factor': random.uniform(0.5, 0.99),
        'epsilon_decay': random.uniform(0.99, 0.999),
    }


def train_with_params(learning_rate, discount_factor, epsilon_decay):
    q_tables = [initialize_q_table(grid_size) for _ in range(num_targets + 1)]
    
    rewards_per_episode = train_agent(environment,
                                    q_tables,
                                    None, 
                                    targets,
                                    learning_rate=learning_rate,
                                    discount_factor=discount_factor,
                                    epsilon_decay=epsilon_decay)
    return mean(rewards_per_episode)

def objective(trial):
    learning_rate = trial.suggest_float("learning_rate", 0.01, 0.5)
    discount_factor = trial.suggest_float("discount_factor", 0.5, 0.99)
    epsilon_decay = trial.suggest_float("epsilon_decay", 0.9, 0.9999)

    # Train agent with these parameters
    total_reward = train_with_params(learning_rate, discount_factor, epsilon_decay)
    return total_reward

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)
print(study.best_params)

