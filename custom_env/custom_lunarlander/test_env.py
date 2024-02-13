import sys
import os
current_directory = os.getcwd()
sys.path.append(str(current_directory))

import lunarlander_folder
import gym
import numpy as np
env = gym.make('myLunarLander-v1')
observation_space = env.observation_space

# Print the observation space
print("Observation Space:", observation_space)