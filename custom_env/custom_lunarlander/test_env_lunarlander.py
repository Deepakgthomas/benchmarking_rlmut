import sys
import os
current_directory = os.getcwd()
sys.path.append(str(current_directory))
from stable_baselines3 import PPO

import lunarlander_folder
import gym
import numpy as np
env = gym.make('myLunarLander-v1')
observation_space = env.observation_space

# Print the observation space
print("Observation Space:", observation_space)

model = PPO.load("best_model.zip")
print(" model.observation_space = ", model.observation_space)
