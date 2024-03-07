import sys
import os
current_directory = os.getcwd()
sys.path.append(str(current_directory))

import cartpole_folder
import gym
import numpy as np
env = gym.make('myCartPole-v1')
for i in range(100):
    observation = env.reset()
    print("i = ", i, " observation = ", observation)
